<template>
  <Bar :chart-data="chartData" />
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: 'BoxPlotChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [40, 20, 12],
          },
        ],
      },
    };
  },
};

</script>


<!--
import "chartjs-chart-box-and-violin-plot";
import { generateChart, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

const BoxPlot = generateChart("boxplot", "boxplot");

export default {
  extends: BoxPlot,
  mixins: [reactiveProp],
  props: ["options"],
  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options);
  }
};-->
