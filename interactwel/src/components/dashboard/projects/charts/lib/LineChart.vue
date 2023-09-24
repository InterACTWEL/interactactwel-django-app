<template>
  <LineChartGenerator
    v-if="chartData != null"
    :chart-data="chartData"
    :chart-options="options"
  />
</template>

<script>

import { Line as LineChartGenerator} from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement,
} from 'chart.js';

ChartJS.register(Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement
);

export default {
  name: 'LineChart',
  components: { LineChartGenerator },
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
import { Line, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {
  extends: Line,
  mixins: [reactiveProp],

  props: {
    chartData: {
      type: Array | Object,
      required: false,
    },
    options: {},
  },

  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options);
  },
};-->
