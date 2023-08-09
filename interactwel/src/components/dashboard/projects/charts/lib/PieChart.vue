<template>
  <Bar :chart-data="chartData" />
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: 'PieChart',
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
