<template>
  <div>
    <v-chart class="chart" :option="option" autoresize />
  </div>
</template>

<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import { TitleComponent, TooltipComponent, LegendComponent } from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, provide } from "vue";
import { onMounted } from "vue";
use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

provide(THEME_KEY, "dark");

const option = ref({
  backgroundColor: "rgb(74, 96, 144)",
  legend: {
    data: ["音乐评论时间分布"],
    icon: "circle",
    right: "10",
    textStyle: {
      color: "rgba(250,250,250,0.6)",
      fontSize: 16,
    },
  },
  radar: [
    {
      radius: "60%",
      name: {
        textStyle: {
          color: "rgba(250,250,250,0.6)",
          fontSize: 16,
        },
      },
      indicator: [
        {
          name: "00:00 - 04:00",
          min: 0,
        },
        {
          name: "04:00 - 08:00",
          min: 0,
        },
        {
          name: "08:00 - 12:00",
          min: 0,
        },
        {
          name: "12:00 - 16:00",
          min: 0,
        },
        {
          name: "16:00 - 20:00",
          min: 0,
        },
        {
          name: "20:00 - 23:59",
          min: 0,
        },
      ],
      center: ["50%", "50%"], // 位置
      shape: "circle", //形状
      splitArea: {
        areaStyle: {
          color: "transparent", //圆环颜色
          shadowColor: "aqua", // 圆颜色
          shadowBlur: 10,
        },
      },
      axisLine: {
        lineStyle: {
          color: "#08585F", // 分割线
        },
      },
      splitLine: {
        lineStyle: {
          color: "#08585F", //圆线
          width: 2,
        },
      },
    },
  ],
  series: [
    {
      type: "radar",
      data: [
        {
          value: [67, 19, 113, 152, 178, 213],
          name: "音乐评论时间分布",
          itemStyle: {
            color: "#327BFA",
            opacity: 0,
          },
          lineStyle: {
            width: 0,
            type: "dotted",
          },
          areaStyle: {
            normal: {
              color: {
                type: "radial",
                x: 0.5,
                y: 0.5,
                r: 0.5,
                colorStops: [
                  {
                    offset: 0,
                    color: "rgba(50, 123, 250, 0.7)", // 0% 处的颜色
                  },
                  {
                    offset: 1,
                    color: "rgba(50, 123, 250, 0.3)", // 100% 处的颜色
                  },
                ],
                global: false, // 缺省为 false
              },
            },
          },
        },
        {
          value: [67, 19, 113, 152, 178, 213],
        },
      ],
    },
  ],
});
</script>

<style scoped>
.chart {
  height: 80vh;
}
</style>
