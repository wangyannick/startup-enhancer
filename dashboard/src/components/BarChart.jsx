import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export function BarChart({ data }) {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
  };

  const dataChart = {
    labels: [...data.map((item) => item.status)],
    datasets: [
      {
        label: "Total funding in USD",
        data: [...data.map((item) => item.funding_total_usd)],
        backgroundColor: "rgba(255, 99, 132, 0.5)",
        borderColor: "rgb(0, 0, 0)",
      },
    ],
  };

  return <Bar options={options} data={dataChart} />;
}
