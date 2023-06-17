<template>
  <div>
    <apexchart
      type="boxPlot"
      :options="chartOptions"
      :series="chartSeries"
      :errorbars="errorbars"
      width="500"
      height="400"
    />
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts';
import ApexCharts from 'apexcharts';


export default {
  name: 'ApexTempBoxplotGraph',
  components: {
    VueApexCharts,
    ApexCharts,
  },
  mixins: [reactiveData],
  props: {
    selectedBasinID: {
      type: String,
    },
    baseGraph: Boolean,
  },

  data() {
    return {
      chartOptions: {
        chart: {
          type: 'boxPlot',
          toolbar: {
            show: false,
          },
        },
        series: [],
        xaxis: {
          categories: ['Category 1', 'Category 2', 'Category 3'],
        },
        errorbars: {
          enabled: true,
          type: 'standard',
          color: '#000',
          thickness: 1,
        },
      },
      chartSeries: [
        {
          name: 'Series 1',
          data: [
            {
              x: 'Category 1',
              y: [10, 20, 30, 40, 50],
            },
            {
              x: 'Category 2',
              y: [15, 25, 35, 45, 55],
            },
            {
              x: 'Category 3',
              y: [18, 28, 38, 48, 58],
            },
          ],
        },
      ],
    };
  },
};
</script>


  