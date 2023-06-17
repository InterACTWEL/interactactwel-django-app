<template>
  <box-plot-chart
    :chart-data="datacollection"
    :options="options"
    :width="320"
    :height="350"
  />
</template>

<script>
import axios from 'axios';
import { BoxPlot, mixins } from 'vue-chartjs';

export default {
  name: 'TempBoxplotGraph',
  extends: BoxPlot,
  mixins: [mixins.reactiveData],
  props: {
    selectedBasinID: {
      type: String,
    },
    baseGraph: Boolean,
  },

  data() {
    return {
      planId: "1",
      JSONData: null,
      datacollection: null,
      graphColors: ["#28a745", "#28a745", "#28a745"],
      options: {
        responsive: true,
        title: {
          display: false,
          text: 'Temperature contribution to stream in watershed.',
        },
        scales: {
          x: {
            display: true,
            stacked: false,
            title: {
              display: true,
              text: 'Years',
            },
          },
          y: {
            display: true,
            stacked: false,
            title: {
              display: true,
              text: 'Celsius',
            },
          },
        },
      },
    };
  },

  mounted() {
    this.planId = this.$route.params.planId;
    this.getData();
  },

  methods: {
    async getData() {
      try {
        const response = await axios.get("/static/et.json");
        this.JSONData = response.data;
        this.buildDataCollection();
      } catch (error) {
        console.error(error);
      }
    },

    buildDataCollection() {
      this.datacollection = {
        labels: this.JSONData.Legend,
        datasets: [],
      };

      const dataset = {
        label: this.JSONData.Description,
        data: [],
        backgroundColor: this.graphColors[0],
      };

      const plan = this.getPlanDataById(this.JSONData, this.planId, this.baseGraph);

      for (const dataIndex in plan.Data) {
        const dataPoint = plan.Data[dataIndex];
        dataset.data.push(dataPoint);
      }

      this.datacollection.datasets.push(dataset);
    },

    getPlanDataById(data, planId, baseGraph) {
      for (const plan in data.Adaptation_Plans) {
        const planObj = data.Adaptation_Plans[plan];
        if (baseGraph && planObj.planId === null) {
          return data.Adaptation_Plans[plan];
        }
        if (planObj.planId === planId) {
          return data.Adaptation_Plans[plan];
        }
      }
    },

    getColor(i) {
      return this.graphColors[i];
    },
  },
};
</script>
