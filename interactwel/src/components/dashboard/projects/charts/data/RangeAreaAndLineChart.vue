<script>
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
    var dataPoints = [
    { x: new Date(2019, 0, 1), y: [-22.4332, 1.701, 26.701] },
              { x: new Date(2019, 1, 1), y: [-22.8482, 6.701, 29.9354] },
              { x: new Date(2019, 2, 1), y: [-16.5272, 9.701, 33.1793] },
              { x: new Date(2019, 3, 1), y: [-10.3894, 11.701, 39.6753] },
              { x: new Date(2019, 4, 1), y: [-13.1862, 13.701, 38.289] },
              { x: new Date(2019, 5, 1), y: [-2.9892, 15.701, 46.6849] },
              { x: new Date(2019, 6, 1), y: [2.20233, 16.701, 47.2412] },
              { x: new Date(2019, 7, 1), y: [0.975366, 15.701, 47.4759] },
              { x: new Date(2019, 8, 1), y: [-6.26288, 18.701, 46.0959] },
              { x: new Date(2019, 9, 1), y: [-9.87604, 20.701, 37.9325] },
              { x: new Date(2019, 10, 1), y: [-21.6, 14.701, 33.2763] },
              { x: new Date(2019, 11, 1), y: [-19.3211, 3.701, 27.0527] }
    ];
    var dps1 = [], dps2 = [];

    for(var i = 0; i < dataPoints.length; i++) {
      dps1.push({x: dataPoints[i].x, y:[dataPoints[i].y[0], dataPoints[i].y[2]]});
      dps2.push({x: dataPoints[i].x, y:dataPoints[i].y[1]});
    }

    this.options.data[0].dataPoints = dps1;
    this.options.data[1].dataPoints = dps2;
  }
}
</script>

<template>
  <CanvasJSChart :options="options" :style="styleOptions"/>
</template>
