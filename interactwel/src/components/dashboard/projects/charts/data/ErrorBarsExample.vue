<template>
  <canvas id="canvas"></canvas>
</template>


<script>
import axios from 'axios';
import { BarWithErrorBarsChart } from 'chartjs-chart-error-bars';

export default {
  name: "ErrorBarsExample",
  data() {
    return {
      chartData: null
    }
  },
  mounted() {
    axios.get("/static/stream-temp-boxplot.json").then(response => {
      this.chartData = response.data;
      this.createChart();
    });
  },
  methods: {
    createChart() {
      const chart = new BarWithErrorBarsChart(document.getElementById('canvas').getContext('2d'), {
        data: {
          labels: this.chartData.labels,
          datasets: [
            {
              data: this.chartData.datasets.map(dataset => ({
                y: dataset.y,
                yMin: dataset.yMin,
                yMax: dataset.yMax,
              })),
            },
          ],
        },
      });
      return chart;
    }
  }
};
</script>

