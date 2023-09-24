<template>
  <div>
    <apexchart
      type="boxPlot"
      :options="chartOptions"
      :series="chartSeries"
      :errorbars="errorbars"
      width="300"
      height="300"
    />
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts';

export default {
  name: 'ApexTempBoxplotGraph',
  components: {
    VueApexCharts,
  },
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
            colors: {
              upper: '#5C4742',
              lower: '#5C4742',
            },
          },
        },
        errorbars: {
          enabled: true,
          type: 'standard',
          color: '#000',
          lineWidth: 1,
        },
      },
      chartSeries: [
        {
          name: 'Year',
          data: [
            {
              x: '2001',
              y: [10, 29.9, 30, 30.1, 70.0],
              color: '#5C4742',
            },
            {
              x: '2002',
              y: [15.1, 25.4, 26.1, 27.4, 45.0],
              color: '#5C4742',
            },
            {
              x: '2003',
              y: [18, 28.1, 28.7, 29.2, 58],
              color: '#5C4742',
            },
          ],
        },
      ],
    };
  },
}
</script>
