<template>
 <line-chart
      :chart-data="datacollectionHHH"
      :options="optionsHHH"
      :width="687"
      :height="120"
    />
</template>

<script>
import axios from 'axios';
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
      JSONData: null,
      datacollection: null,
      graphColors: [
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
          intersect: true,
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
              labelString: 'deg C',
            },
          }],
        },
      },
    };
  },

  mounted() {
    this.planId = this.$route.params.planId;
    this.buildDataCollection(this.JSONData, this.planId);
  },

  created() {
    axios.get("/static/wtmpdegcStreamGraph.json").then(response => {
      this.JSONData = response.data;
      this.buildDataCollection(this.JSONData, this.planId);
    });
  },

  methods: {
    buildDataCollection(data, adaptationPlan) {
      this.datacollection = {};
      this.datacollection.labels = [];
      for (let legend in data.Legend) {
        this.datacollection.labels.push(data.Legend[legend]);
      }

      this.datacollection.datasets = [];

      let dataset = {};
      dataset.data = [];
      dataset.label = data.Description;
      dataset.backgroundColor = this.getColor(0);

      adaptationPlan = this.baseGraph ? 'BASE' : adaptationPlan;
      const regionData = data['Adaptation_Plans']['Adaptation Plan ' + adaptationPlan]['region ' + this.selectedBasinId]['Data'];

      for (let dataIndex in regionData) {
        let dataPoint = regionData[dataIndex];
        dataset.data.push(dataPoint);
      }

      this.datacollection.datasets.push(dataset);

    },

    showChart: function(selectedPlan) {
      this.planName = selectedPlan;
    },

    getColor(i) {
      let color;
      color = this.graphColors[i];
      return color;
    },
  },
  watch: {
    selectedBasinId: function() {
      this.buildDataCollection(this.JSONData, this.planId);
    },
  },
};
</script>
