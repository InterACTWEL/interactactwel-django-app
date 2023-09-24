<template>
  <Bar
    v-if="chartData != null"
    :chart-data="chartData"
    :chart-options="options"
  />
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: 'BoxPlotChart',
  components: { Bar },
  props: {
    chartData: {
      type: Object,
      required: false,
    },
    options: {},
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
