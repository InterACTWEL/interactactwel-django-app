<template>
  <Pie
    v-if="chartData != null"
    :chart-data="chartData"
    :chart-options="options"
  />
</template>

<script>
import { Pie } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  LineElement,
  CategoryScale,
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, ArcElement, LineElement, CategoryScale);

export default {
  name: 'PieChart',
  components: { Pie },
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
import { Pie, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins;

export default {
  extends: Pie,
  mixins: [reactiveProp],

  props: {
    chartData: {
      type: Array | Object,
      required: false,
    },
    options: {
    },
  },

  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options);
  },
};-->
