<script>
import axios from 'axios';
import CanvasJSChart from '@/components/CanvasJSVueComponent.vue';

export default {
  components: {
    CanvasJSChart
  },
  data() {
    return {
      chart: null,
      options: {
        title: {
          text: "RangeArea Chart With Average Line Series"
        },
        data: [
          {
            type: "rangeArea",
            dataPoints: []
          },
          {
            type: "line",
            dataPoints: []
          }
        ]
      },
      styleOptions: {
        width: "100%",
        height: "360px"
      }
    }
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get("/static/stream-temperature-data.json").then(response => {
        var dataPoints = response.data;
        var dps1 = [], dps2 = [];

        for(var i = 0; i < dataPoints.length; i++) {
          dps1.push({x: new Date(dataPoints[i].x), y:[dataPoints[i].y[0], dataPoints[i].y[2]]});
          dps2.push({x: new Date(dataPoints[i].x), y:dataPoints[i].y[1]});
        }

        this.options.data[0].dataPoints = dps1;
        this.options.data[1].dataPoints = dps2;
      });
    }
  }
}
</script>

<template>
  <CanvasJSChart :options="options" :style="styleOptions"/>
</template>
