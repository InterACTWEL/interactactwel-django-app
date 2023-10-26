<template>
  <CanvasJSChart :options="options" 
  :style="styleOptions" 
  @chart-ref="chartInstance" />
</template>

<script>
import CanvasJSChart from '@/components/CanvasJSVueComponent.vue';
import axios from 'axios';

export default {
  name: "TemperatureChart",
  components: {
    CanvasJSChart,
  },
  data() {
    return {
      chart: null,
      options: {
        exportEnabled: true,
        title: {
          text: "Temperature Variation",
        },
        subtitles: [{
          text: "California, USA",
        }],
        axisY: {
          title: "Temperature (°C)",
          suffix: "°C",
        },
        axisX: {
          interval: 1,
          intervalType: "month",
          valueFormatString: "MMM",
        },
        toolTip: {
          shared: true,
        },
        legend: {
          cursor: "pointer",
          itemclick: this.toggleDataSeries,
        },
        data: [{
          type: "rangeArea",
          showInLegend: true,
          name: "Temperature Range",
          yValueFormatString: "##.0 °C",
          xValueFormatString: "MMMM YYYY",
          toolTipContent: "{x}<br><span style='color:{color}'>Min</span>: {y[0]}<br><span style='color:{color}'>Max</span>: {y[1]}",
          xValueType: "dateTime",
          markerSize: 0,
          dataPoints: []
        }],
      },
      styleOptions: {
        width: "100%",
        height: "360px",
      },
    };
  },
  mounted() {
    axios.get("/static/stream-temperature-data.json").then(response => {
      const dataPoints = response.data.map(item => ({
        x: new Date(item.date),
        y: [item.min, item.max],
        Average: (item.min + item.max) / 2, // Added the Average key to the dataPoints array
      }));
      this.options.data[0].dataPoints = dataPoints; // Added the Average key to the options.data[0].dataPoints array
      this.chart.render();
    });
  },
  methods: {
    toggleDataSeries(e) {
      if (typeof e.dataSeries.visible === "undefined" || e.dataSeries.visible) {
        e.dataSeries.visible = false;
      } else {
        e.dataSeries.visible = true;
      }
      e.chart.render();
    },
    addAverageSeries() {
      let dps = [];
      let chart = this.chart;
      for (let i = 0; i < chart.options.data[0].dataPoints.length; i++) {
        const dataPoint = chart.options.data[0].dataPoints[i];
        dps.push({
          x: dataPoint.x,
          y: dataPoint.Average, // Use the "Average" value from the JSON
        });
      }
      chart.options.data.push({
        type: "line",
        name: "Average",
        showInLegend: true,
        visible: true, // Added the visible: true property
        markerType: "triangle",
        markerSize: 0,
        color: "blue",
        yValueFormatString: "##.0 °C",
        toolTipContent: "<span style='color:{color}'>{name}</span>: {y}",
        dataPoints: dps,
      });
      chart.render();
    },
    chartInstance(chart) {
      this.chart = chart;
      this.addAverageSeries();
    },
  },
};
</script>