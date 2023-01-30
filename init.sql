CREATE TABLE Startup (
  id SERIAL PRIMARY KEY,
  permalink TEXT,
  name TEXT,
  homepage_url TEXT,
  category_list TEXT,
  funding_total_usd TEXT,
  status TEXT,
  country_code TEXT,
  state_code TEXT,
  region TEXT,
  city TEXT,
  funding_rounds TEXT,
  founded_at DATE,
  first_funding_at DATE,
  last_funding_at DATE
);

