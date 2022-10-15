(function ($) {
  /* "use strict" */

  var dzChartlist = (function () {
    let draw = Chart.controllers.line.__super__.draw; //draw shadow
    var screenWidth = $(window).width();

    var chartBar1 = function () {
      var options1 = {
          series: [
            {
              data:chart_data_1
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-1"),
          options1
        );
      chart1.render();
    };

    var chartBar2 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_2,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-2"),
          options2
        );
      chart2.render();
    };
    var chartBar3 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_3,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-3"),
          options2
        );
      chart2.render();
    };
    var chartBar4 = function () {
      var options1 = {
          series: [
            {
              data:chart_data_4,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-4"),
          options1
        );
      chart1.render();
    };
    var chartBar5 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_5,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-5"),
          options1
        );
      chart1.render();
    };
    var chartBar6 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_6,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-6"),
          options2
        );
      chart2.render();
    };
    var chartBar7 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_7,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-7"),
          options1
        );
      chart1.render();
    };
    var chartBar8 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_8,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-8"),
          options1
        );
      chart1.render();
    };
    var chartBar9 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_9,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-9"),
          options1
        );
      chart1.render();
    };

    var chartBar10 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_10,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-10"),
          options2
        );
      chart2.render();
    };
    var chartBar11 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_11,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-11"),
          options2
        );
      chart2.render();
    };
    var chartBar12 = function () {
      var options1 = {
          series: [
            {
              data:chart_data_12,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-12"),
          options1
        );
      chart1.render();
    };
    var chartBar13 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_13,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-13"),
          options1
        );
      chart1.render();
    };
    var chartBar14 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_14,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-14"),
          options2
        );
      chart2.render();
    };
    var chartBar15 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_15,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-15"),
          options1
        );
      chart1.render();
    };
    var chartBar16 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_16,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-16"),
          options1
        );
      chart1.render();
    };
    var chartBar17 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_17,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-17"),
          options2
        );
      chart2.render();
    };
    var chartBar18 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_18,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-18"),
          options2
        );
      chart2.render();
    };
    var chartBar19 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_19,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-19"),
          options1
        );
      chart1.render();
    };
    var chartBar20 = function () {
      var options1 = {
          series: [
            {
              data: chart_data20,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-20"),
          options1
        );
      chart1.render();
    };
    var chartBar21 = function () {
      var options2 = {
          series: [
            {
              data: chart_data_21,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-21"),
          options2
        );
      chart2.render();
    };
    var chartBar22 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_22,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-22"),
          options1
        );
      chart1.render();
    };
    var chartBar23 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_23,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-23"),
          options1
        );
      chart1.render();
    };
    var chartBar24 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_24,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-24"),
          options1
        );
      chart1.render();
    };
    var chartBar25 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_25,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-25"),
          options1
        );
      chart1.render();
    };
    var chartBar26 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_26,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-26"),
          options1
        );
      chart1.render();
    };
    var chartBar27 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_27,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-27"),
          options1
        );
      chart1.render();
    };
    var chartBar28 = function () {
      var options1 = {
          series: [
            {
              data: chart_data_28,
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
           marker: { show: !1 },
              theme: 'dark'
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-28"),
          options1
        );
      chart1.render();
    };



    /* Function ============ */
    return {
      init: function () {},

      load: function () {
        chartBar1();
        chartBar2();
        chartBar3();
        chartBar4();
        chartBar5();
        chartBar6();
        chartBar7();
        chartBar8();
        chartBar9();
        chartBar10();
        chartBar11();
        chartBar12();
        chartBar13();
        chartBar14();
        chartBar15();
        chartBar16();
        chartBar17();
        chartBar18();
        chartBar19();
        chartBar20();
        chartBar21();
        chartBar22();
        chartBar23();
        chartBar24();
        chartBar25();
        chartBar26();
        chartBar27();
        chartBar28();
      },

      resize: function () {},
    };
  })();

  jQuery(document).ready(function () {});

  jQuery(window).on("load", function () {
    setTimeout(function () {
      dzChartlist.load();
    }, 1000);
  });

  jQuery(window).on("resize", function () {});
})(jQuery);
