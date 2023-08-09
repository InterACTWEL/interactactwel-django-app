<template>
  <canvas id="canvas"></canvas>
</template>

<script>
import Chart from "chart.js";
import 'chartjs-chart-error-bars';

export default {
  name: "ErrorBarsExample",
  mounted() {
    let chart = new Chart(document.getElementById("canvas").getContext("2d"), {
      type: "barWithErrorBars",
      data: {
        labels: ["A", "B"],
        datasets: [
          {
            data: [
              {
                y: 4,
                yMin: 1,
                yMax: 6,
              },
              {
                y: 2,
                yMin: 1,
                yMax: 4,
              },
            ],
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
    return chart;
  },
};
</script>

<style scoped>
canvas {
  -moz-user-select: none;
  -webkit-user-select: none;
  -ms-user-select: none;
}
</style>
