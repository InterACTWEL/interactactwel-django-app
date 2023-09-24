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
          exportEnabled: true,
          title: {
            text: "Temperature Variation"
          },
          subtitles: [{
            text: "California, USA"
          }],
          axisY: {
            title: "Temparature (°C)",
            suffix: "°C"
          },
          axisX: {
            interval: 1,
            intervalType: "month",
            valueFormatString: "MMM",
          },
          toolTip: {
            shared: true
          },
          legend: {
            cursor: "pointer",
            itemclick: this.toggleDataSeries
          },
          data: [{
            type: "rangeArea",
            showInLegend: true,
            name: "Temperature Range",
            yValueFormatString: "##.0 °C",
            xValueFormatString: "MMMM YYYY",
            toolTipContent: "{x}<br><span style='\"'color:{color}'\"'>Min</span>: {y[0]}<br><span style='\"'color:{color}'\"'>Max</span>: {y[1]}",
            xValueType: "dateTime",
            markerSize: 0,
            dataPoints: [
              { x: new Date(2019, 0, 1), y: [-22.4332, 26.701] },
              { x: new Date(2019, 1, 1), y: [-22.8482, 29.9354] },
              { x: new Date(2019, 2, 1), y: [-16.5272, 33.1793] },
              { x: new Date(2019, 3, 1), y: [-10.3894, 39.6753] },
              { x: new Date(2019, 4, 1), y: [-13.1862, 38.289] },
              { x: new Date(2019, 5, 1), y: [-2.9892, 46.6849] },
              { x: new Date(2019, 6, 1), y: [2.20233, 47.2412] },
              { x: new Date(2019, 7, 1), y: [0.975366, 47.4759] },
              { x: new Date(2019, 8, 1), y: [-6.26288, 46.0959] },
              { x: new Date(2019, 9, 1), y: [-9.87604, 37.9325] },
              { x: new Date(2019, 10, 1), y: [-21.6, 33.2763] },
              { x: new Date(2019, 11, 1), y: [-19.3211, 27.0527] }
            ]
          }]
        },
        styleOptions: {
          width: "100%",
          height: "360px"
        }
      }
    },
    methods: {
      toggleDataSeries(e) {
        if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
          e.dataSeries.visible = false;
        }
        else {
          e.dataSeries.visible = true;
        }
        e.chart.render();
      },
      addAverageSeries() {
        let dps = [];
        let chart = this.chart;
        for(let i = 0; i < chart.options.data[0].dataPoints.length; i++) {
          dps.push({
            x: chart.options.data[0].dataPoints[i].x,
            y: (chart.options.data[0].dataPoints[i].y[0] + chart.options.data[0].dataPoints[i].y[1]) / 2
          });
        }
        chart.options.data.push({
          type: "line",
          name: "Average",
          showInLegend: true,
          markerType: "triangle",
          markerSize: 0,
          color: "#EF5350",
          yValueFormatString: "##.0 °C",
          toolTipContent: "<span style='\"'color:{color}'\"'>{name}</span>: {y}",
          dataPoints: dps
        });
        chart.render();
      },
      chartInstance(chart) {
        this.chart = chart;
        this.addAverageSeries();
      }
    }
  }
</script>
  
<template>
    <CanvasJSChart :options="options" :style="styleOptions" @chart-ref="chartInstance"/>
</template>                              