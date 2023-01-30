import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getStartups, getMedians } from "../services/api";
import { PieChart } from "../components/PieChart";
import { BarChart } from "../components/BarChart";
import "../css/Dashboard.css";
import { BarChartMedian } from "../components/BarChartMedian";

function Dashboard() {
  const params = useParams();
  const [state, setState] = useState({
    startups: [],
    status: [],
    info: {
      total: 0,
      still_operating: 0,
    },
  });

  const [median, setMedian] = useState([]);

  useEffect(() => {
    async function init() {
      const startups = await getStartups(params.category, params.country);
      setState(startups);

      const medians = await getMedians(params.country);
      setMedian(medians);
    }

    init();
  }, [params.category, params.country]);

  return (
    <div>
      <h1>
        {params.category} - {params.country}
      </h1>

      <h2>
        Total of {state.info.total} startups in {params.category} in{" "}
        {params.country}, with {state.info.still_operating} still operating.
      </h2>

      {state.startups.length > 0 && state.status.length > 0 && (
        <div className="graphs">
          <PieChart data={state.status} />
          <BarChart data={state.status} />
        </div>
      )}

      {median.length > 0 && (
        <>
          <h2
            style={{
              marginTop: 120,
            }}
          >
            Type of startups that works in {params.country}:
          </h2>

          <div className="median">
            <BarChartMedian data={median} />
          </div>
        </>
      )}
    </div>
  );
}

export default Dashboard;
