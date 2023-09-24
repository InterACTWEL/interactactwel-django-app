<template>
    <LineChartGenerator
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
    />
</template>
  
<script>
import { Line as LineChartGenerator } from 'vue-chartjs/legacy'
  
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    CategoryScale,
    PointElement
} from 'chart.js'
  
ChartJS.register(
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    CategoryScale,
    PointElement
)
  
export default {
    name: 'LineChart',
    components: {
      LineChartGenerator
    },
    props: {
      chartId: {
        type: String,
        default: 'line-chart'
      },
      datasetIdKey: {
        type: String,
        default: 'label'
      },
      width: {
        type: Number,
        default: 400
      },
      height: {
        type: Number,
        default: 400
      },
      cssClasses: {
        default: '',
        type: String
      },
      styles: {
        type: Object,
        default: () => {}
      },
      plugins: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        chartData: {
          labels: ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
          datasets: [
            {
              label: 'Average',
              data: [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
              borderColor: 'black',
              borderWidth: 2,
              tension: 0.5,
              fill: 1
            },
            {
              label: 'Maximum',
              data: [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
              borderColor: 'blue',
              borderWidth: 2,
              backgroundColor: "rgba(0, 0, 255, 0.5)", // blue with 50% opacity
              tension: 0.5, 
              fill: 'false'
            },
            {
              label: 'Minimum',
              data: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
              borderColor: 'green',
              borderWidth: 2,
              backgroundColor: "rgba(0, 0, 255, 0.5)", // blue with 50% opacity
              tension: 0.5, 
              fill: 1
            },
          ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
}
</script>
