<template>
  <canvas id="canvas" />
</template>

<script>
import { BarWithErrorBarsChart } from 'chartjs-chart-error-bars';

export default {
  name: "ErrorBarsExample",
  mounted() {
    const chart = new BarWithErrorBarsChart(document.getElementById('canvas').getContext('2d'), {
      data: {
        labels: ['A', 'B'],
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
