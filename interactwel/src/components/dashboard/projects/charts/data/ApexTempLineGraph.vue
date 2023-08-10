<template>
  <line-chart
    :chart-data="datacollection"
    :options="options"
    :width="800"
    :height="600"
  />
  
</template>

<script>
import LineChart from "../lib/LineChart.js";

export default {
  name: 'ApexTempLineGraph',
  components: {
    LineChart,
  },
  props: {
    selectedBasinId: {
      name: String,
    },
    baseGraph: Boolean,
  },

  data() {
    return {
      planId: 1,
      datacollection: null,
      graphColors: [
        "#28a745",
        "#28a745",
        "#28a745",
      ],
      options: {
        responsive: true,
        title: {
          display: false,
          text: 'Stream Temperature',
        },
        tooltips: {
          mode: 'point',
          intersect: false,
        },
        hover: {
          mode: 'nearest',
          intersect: false,
        },
        legend: {
          show: false
        },
        scales: {
          xAxes: [{
            display: true,
            stacked: false,
            scaleLabel: {
              display: true,
              labelString: 'Years',
            },
          }],
          yAxes: [{
            display: true,
            stacked: false,
            scaleLabel: {
              display: true,
              labelString: 'Stream Temperature ',
            },
          }],
        },
      },
    };
  },

  mounted() {
    this.planId = this.$route.params.planId;
    this.buildDataCollection();
  },

  created() {
    this.buildDataCollection();
  },

  methods: {
    buildDataCollection() {
      this.datacollection = {};
      this.datacollection.labels = ['2020', '2021', '2022', '2023', '2024', '2025'];
      this.datacollection.datasets = [];

      let dataset = {};
      dataset.data = [];
      dataset.label = false;
      dataset.backgroundColor = 'rgba(40, 167, 69, 0.5)';
      dataset.fill = '-1';
      // dataset.pointRadius = 0;
      // dataset.borderWidth = 1;

      this.datacollection.datasets.push(dataset);

      // Add minimum line
      let minDataset = {};
      minDataset.data = [10, 12, 10, 14, 16, 14];
      minDataset.label = false;
      minDataset.borderColor = '#28a745';
      minDataset.borderWidth = 2;
      minDataset.fill = '-1';

      this.datacollection.datasets.push(minDataset);

      // Add average line
      let avgDataset = {};
      avgDataset.data = [12.5, 13.75, 12.5, 16.25, 18.75, 16.25];
      avgDataset.label = false;
      avgDataset.borderColor = this.getColor(2);
      avgDataset.borderWidth = 3;
      avgDataset.fill = '-1';

      this.datacollection.datasets.push(avgDataset);

      // Add maximum line
      let maxDataset = {};
      maxDataset.data = [15, 17, 15, 20, 22, 20];
      maxDataset.label = false;
      maxDataset.borderColor = '#28a745';
      // maxDataset.borderWidth = 4;
      maxDataset.fill = '-1';

      this.datacollection.datasets.push(maxDataset);
    },

    getColor(i) {
      let color;
      color = this.graphColors[i];
      return color;
    },
  }, 
};
</script>

