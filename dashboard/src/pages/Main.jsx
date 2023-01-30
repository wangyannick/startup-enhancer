import { useEffect, useState } from "react";
import "../css/Main.css";
import MultipleSelect from "../components/Select";
import { getCountries, getCategories } from "../services/api";

import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
});

function Main() {
  let navigate = useNavigate();
  const [state, setState] = useState({
    countries: [],
    categories: [],
  });

  useEffect(() => {
    async function init() {
      const countries = await getCountries();
      const categories = await getCategories();

      setState({
        countries,
        categories,
      });
    }

    init();
  }, []);

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />

      <div className="dashboard">
        <h1>Startup launcher 🚀</h1>
        {state.countries && state.categories && (
          <div className="dashboard--selects">
            <MultipleSelect placeholder={"Category"} items={state.categories} />
            <MultipleSelect placeholder={"Country"} items={state.countries} />
          </div>
        )}

        <Button
          variant="contained"
          size="large"
          onClick={() => navigate("/dashboard")}
        >
          Validate
        </Button>
      </div>
    </ThemeProvider>
  );
}

export default Main;
