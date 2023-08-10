<template>
  <apexchart type="line" :options="chartOptions" :series="chartSeries" />
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: "forecast-line-chart",
        },
        xaxis: {
          categories: ["2020", "2021", "2022", "2023", "2024", "2025"],
        },
        fill: {
          type: "gradient",
          opacity: 0.5,
        },
        markers: {
          size: 0,
        },
        dataLabels: {
          enabled: false,
        },
        tooltip: {
          enabled: false,
        },
        colors: ["#28a745"],
        grid: {
          borderColor: "#f1f1f1",
        },
        yaxis: {
          title: {
            text: "Stream Temperature (°C)",
          },
        },
      },
      chartSeries: [
        {
          name: "Average",
          data: [12.5, 13.75, 12.5, 16.25, 18.75, 16.25],
          fill: {
            type: "gradient",
            opacity: 1,
            colors: ["#28a745"],
          },
          stroke: {
            width: 3,
            curve: "smooth",
          },
        },
        {
          name: "Minimum",
          data: [10, 12, 10, 14, 16, 14],
          fill: {
            type: "gradient",
            opacity: 0.3,
            colors: ["#28a745", 'transparent'],
          },
          stroke: {
            width: 0,
          },
        },
        {
          name: "Maximum",
          data: [15, 17, 15, 20, 22, 20],
          fill: {
            type: "gradient",
            opacity: 0.3,
            colors: ["#28a745", 'transparent'],
          },
          stroke: {
            width: 0, // Set the line width to 0 to make it invisible
          },
        },
      ],
    };
  },
};
</script>


