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

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

provide(THEME_KEY, "dark");

const option = ref({
  backgroundColor: "rgb(77, 100, 150)",
  title: {
    text: "情感分析",
    left: "center",
  },
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b} : {c} ({d}%)",
  },
  legend: {
    orient: "vertical",
    left: "left",
    data: ["积极", "消极"],
  },
  series: [
    {
      name: "情感",
      type: "pie",
      radius: "55%",
      center: ["50%", "60%"],
      data: [
        { value: 619, name: "积极" },
        { value: 181, name: "消极" },
      ],
      emphasis: {
        itemStyle: {},
      },
    },
  ],
});
</script>

<style scoped>
.chart {
  height: 80vh;
}
</style>
