<script>
import CanvasJSChart from '@/components/CanvasJSVueComponent.vue';
  
  export default {  
    components: {
    CanvasJSChart
  },  
    data() {
      return {
        options: {
          colorSet: "colorSet2",
          exportEnabled: true,
          title: {
            text: "Mean Air Temperature vs Mean Relative Humidity",
            fontSize: 15
          },
          axisX: {
            title: "Air Temperature (°C)",
            suffix: " °C"
          },
          axisY: {
            title: "Relative Humidity",
            suffix: "%"
          },
          toolTip: {
            shared: true
          },
          data: [{
            type: "line",
            name: "Relative Humidity",
            toolTipContent: "<strong>Air Temperature:</strong> {x} °C <br> <span style=\"color:#8CA1BC\">Relative Humidity</span>: {y}%",
            dataPoints: [
              { x: 27.1, y: 83.16 },
              { x: 28.2, y: 79.97 },
              { x: 29.0, y: 76.52 },
              { x: 30.0, y: 72.28 },
              { x: 30.9, y: 69.83 },
              { x: 31.9, y: 66.40 },
              { x: 32.9, y: 65.86 },
              { x: 33.9, y: 62.00 },
              { x: 34.9, y: 59.99 }
            ]
          },
          {
            type: "error",
            name: "Error Range",
            toolTipContent: "<span style=\"color:#36845C\">{name}</span>: {y[0]}% - {y[1]}%",
            dataPoints: [
              { x: 27.1, y: [81.84, 85.42] },
              { x: 28.2, y: [78.41, 81.12] },
              { x: 29.0, y: [74.97, 77.85] },
              { x: 30.0, y: [71.08, 74.12] },
              { x: 30.9, y: [66.67, 72.04] },
              { x: 31.9, y: [65.12, 67.46] },
              { x: 32.9, y: [63.94, 67.27] },
              { x: 33.9, y: [60.90, 63.24] },
              { x: 34.9, y: [57.45, 62.08] }
            ]
          }]
        },
        styleOptions: {
          width: "100%",
          height: "360px"
        }
      }
    }
  }
</script>
  
<template>
    <CanvasJSChart :options="options" :style="styleOptions" />
</template>                              