<template>
  <vertical-bar-chart
    :chart-data="datacollection"
    :options="options"
    :width="5"
    :height="3"
  />
</template>

<script>
import axios from 'axios';
import VerticalBarChart from "../lib/VerticalBarChart";

export default {
  name: 'precipSubGraph',
  components: {
    VerticalBarChart,
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
          text: 'Precipitation',
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
              labelString: 'mm',
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
    axios.get("/static/precipSub.json").then(response => {
      this.JSONData = response.data;
      this.buildDataCollection(this.JSONData, this.planId);
    });
  },

  methods: {
    buildDataCollection(data, adaptationPlan) {
      if (!data) {
        return;
      }
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
      const subBasinData = data['Adaptation_Plans']['Adaptation Plan ' + adaptationPlan]['Subbasin ' + this.selectedBasinId]['Data'];

      for (let dataIndex in subBasinData) {
        let dataPoint = subBasinData[dataIndex];
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
