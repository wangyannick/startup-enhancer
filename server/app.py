import psycopg2
import pandas as pd
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import numpy as np
import time
from tqdm import tqdm


conn = None

while conn is None:
    # sleep for 5 seconds
    time.sleep(5)
    try:
        conn = psycopg2.connect(
            "dbname='mydb' user='myuser' host='db' password='mypassword'")
    except:
        print("Database connection error")

if conn is not None:
    cur = conn.cursor()

    cur.execute("""SELECT * from Startup""")

    rows = cur.fetchall()

    if len(rows) == 0:
        print("No rows in Startup, inseting data - this may take a while...")
        df = pd.read_csv('big_startup_secsees_dataset.csv')
        df = df.where((pd.notnull(df)), None)
        df['name'] = df['name'].fillna('NO_NAME')

        data = df.values.tolist()
        # show toolbar of progress

        for row in tqdm(data):
            cur.execute("INSERT INTO Startup (permalink, name, homepage_url, category_list, funding_total_usd, status, country_code, state_code, region, city, funding_rounds, founded_at, first_funding_at, last_funding_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
            conn.commit()
        print("Finished inserting data")

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/api/categories")
def get_categories():
    cur.execute("SELECT DISTINCT category_list FROM Startup")
    categories = cur.fetchall()
    categories_list = []

    for category in categories:
        if category[0]:
            for cat in category[0].split("|"):
                if cat not in categories_list:
                    categories_list.append(cat)

    return {
        "data": categories_list
    }


@app.route("/api/countries")
def get_countries():
    cur.execute("SELECT DISTINCT country_code FROM Startup")
    countries = cur.fetchall()
    countries_list = []

    for country in countries:
        if country[0]:
            countries_list.append(country[0])

    return {
        "data": countries_list
    }


@app.route("/api/states/<countryParams>")
def get_states(countryParams):
    cur.execute(
        "SELECT DISTINCT state_code FROM Startup WHERE country_code = %s", (countryParams,))
    states = cur.fetchall()
    states_list = []

    for state in states:
        if state[0]:
            states_list.append(state[0])

    return {
        "data": states_list
    }


@app.route("/api/startups/<categoryParams>")
@app.route("/api/startups/<categoryParams>/<countryParams>")
@app.route("/api/startups/<categoryParams>/<countryParams>/<stateParams>")
def get_startups(categoryParams, countryParams=None, stateParams=None):
    if stateParams:
        cur.execute("SELECT * FROM Startup WHERE position(%s in category_list) > 0 AND country_code = %s AND state_code = %s",
                    (categoryParams, countryParams, stateParams,))
    elif countryParams:
        cur.execute("SELECT * FROM Startup WHERE position(%s in category_list) > 0 AND country_code = %s",
                    (categoryParams, countryParams,))
    else:
        cur.execute(
            "SELECT * FROM Startup WHERE position(%s in category_list) > 0", (categoryParams,))
    try:
        startups = cur.fetchall()
    except:
        return {
            "data": {
                "startups": [],
                "status": [],
                "info": {
                    "total": 0,
                    "still_operating": 0,
                }
            }
        }

    columns = [desc[0] for desc in cur.description]

    startups_list = []
    for indexStartup, startup in enumerate(startups):
        startup = {}
        for indexColumn, column in enumerate(columns):
            startup[column] = startups[indexStartup][indexColumn]
        startups_list.append(startup)

    if len(startups_list) == 0:
        return {
            "data": {
                "startups": startups_list,
                "status": [],
                "info": {
                    "total": len(startups_list),
                    "still_operating": len([x for x in startups_list if x['status'] == 'operating']),
                }
            }
        }

    df_status = pd.DataFrame(startups_list)
    df_status = df_status.groupby('status').size().reset_index(name='counts')
    df_status['percentage'] = round(
        df_status['counts'] / df_status['counts'].sum() * 100, 1)
    df_status = df_status[['status', 'percentage']]
    df_status = df_status.where((pd.notnull(df_status)), None)
    df_status = df_status.fillna(0)
    df_status = df_status.to_dict('records')

    df_funding = pd.DataFrame(startups_list)
    df_funding['funding_total_usd'] = df_funding['funding_total_usd'].replace(
        '-', None)

    df_funding = df_funding.groupby('status').agg(
        {'funding_total_usd': 'median'}).reset_index()
    df_funding = df_funding.where((pd.notnull(df_funding)), None)
    df_funding = df_funding.to_dict('records')

    merged = []
    for index, row in enumerate(df_status):
        merged.append({**row, **df_funding[index]})

    return {
        "data": {
            "startups": startups_list,
            "status": merged,
            "info": {
                "total": len(startups_list),
                "still_operating": len([x for x in startups_list if x['status'] == 'operating']),
            }
        }
    }


@ app.route("/api/median/<countryParams>")
def get_median(countryParams):
    cur.execute(
        "SELECT category_list FROM Startup WHERE country_code = %s", (countryParams,))

    try:
        categories = cur.fetchall()
    except:
        return {
            "data": []
        }

    categories_list = []

    for category in categories:
        if category[0]:
            for cat in category[0].split("|"):
                if cat not in categories_list:
                    categories_list.append(cat)

    categories_median = []
    for category in categories_list:
        cur.execute(
            "SELECT funding_total_usd FROM Startup WHERE position(%s in category_list) > 0 AND country_code = %s", (category, countryParams))
        funding_total_usd = cur.fetchall()
        funding_total_usd = [float(x[0])
                             for x in funding_total_usd if x[0] != '-' and x[0] != None]
        categories_median.append({
            "category": category,
            "median": np.median(funding_total_usd)
        })

    # keep only the 10 highest median
    categories_median = sorted(
        categories_median, key=lambda k: k['median'], reverse=True)[:10]

    return {
        "data": categories_median
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
