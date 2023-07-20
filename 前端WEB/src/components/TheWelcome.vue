<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import * as echarts from "echarts";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import { TitleComponent, TooltipComponent, LegendComponent } from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, provide } from "vue";

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

provide(THEME_KEY, "dark");

const option = ref({
  backgroundColor: "rgb(77, 100, 150)",
  grid: {
    left: "1%",
    right: "1%",
    top: "10%",
    bottom: "10%",
    containLabel: true,
  },
  xAxis: {
    type: "category",
    boundaryGap: 1,
    axisLine: {
      lineStyle: {
        color: "#ffffff80", //x轴的颜色
      },
    },
    axisTick: {
      show: false, // 隐藏x轴刻度线
      alignWithLabel: true,
    },
    axisLabel: {
      color: "#C5D6E6",
    },
    data: ["广东", "河南", "四川", "山东", "江苏", "浙江", "上海"],
  },
  yAxis: [
    {
      type: "value",
      name: "百分比",
      min: 0,
      splitLine: {
        lineStyle: {
          color: "#ffffff1a",
          type: "dashed",
        },
      },
      max: 20,
      axisLabel: {
        show: true,
        margin: 10,
        color: "#C5D6E6", //y轴字体颜色
      },
      axisTick: {
        alignWithLabel: true,
      },
    },
  ],
  series: [
    {
      data: [11, 9, 8, 7, 7, 4, 4],
      type: "pictorialBar",
      showBackground: true,
      label: {
        show: true,
        position: "top",
        color: "#5797FF",
      },
      backgroundStyle: {
        color: "rgba(255, 255, 255, 0.03)",
      },
      barCategoryGap: "40%",
      // https://echarts.apache.org/zh/option.html#series-pictorialBar.symbol
      symbol: "triangle",
      itemStyle: {
        normal: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#5797FF",
            },
            {
              offset: 1,
              color: "rgba(87,151,255,0)",
            },
          ]),
        },
      },
      emphasis: {
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "#D2FF77",
            },
            {
              offset: 1,
              color: "rgba(210,255,119,0)",
            },
          ]), // 鼠标滑过时柱状图的颜色
          opacity: 1, // 鼠标滑过时柱状图的透明度
        },
        label: {
          show: true, // 鼠标滑过时是否显示标签
          position: "top", // 鼠标滑过时标签位置
          textStyle: {
            color: "#D2FF77", // 鼠标滑过时柱状图的颜色
            opacity: 1, // 鼠标滑过时柱状图的透明度
          },
        },
      },
    },
    {
      type: "bar",
      barWidth: "60%",
      symbol: "path://M0,10 L10,10 C5.5,10 5.5,5 5,0 C4.5,5 4.5,10 0,10 z",
      itemStyle: {
        normal: {
          color: "rgba(255, 255, 255, 0.08)",
        },
      },
      data: [200, 200, 200, 200, 200, 200, 200],
      z: "-99",
    },
    // 带边框的圆圈
    {
      type: "scatter",
      symbolSize: 12,
      zlevel: 13,
      itemStyle: {
        borderWidth: 1,
        borderColor: "#5797FF",
        color: "rgba(0, 0, 0, 0)",
        opacity: 1,
      },
      silent: true,
      data: [120, 200, 150, 80, 70, 110, 130],
    },
    // 实心圆圈
    {
      type: "scatter",
      symbolSize: 6,
      zlevel: 12,
      itemStyle: {
        color: {
          type: "radial",
          r: 1,
          colorStops: [
            {
              offset: 0,
              color: "#fff",
            },
            {
              offset: 1,
              color: "#fff",
            },
          ],
          global: false,
        },
      },
      silent: true,
      data: [120, 200, 150, 80, 70, 110, 130],
    },
  ],
});
</script>

<style scoped>
.chart {
  height: 80vh;
}
</style>
