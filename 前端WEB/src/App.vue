<script setup>
import { RouterLink, RouterView } from "vue-router";
import Ciyun from "./components/ciyun.vue";
import Aside from "./views/Aside.vue";
</script>

<template>
  <Ciyun class="absolute left-20 top-0" />
  <el-card class="box-card absolute left-170 w-150 top-0">
    <template #header>
      <div class="card-header">
        <span style="font-size: large">《花海》评论数据可视化</span>
      </div>
    </template>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">评论地区分布</RouterLink>
        <RouterLink to="/about">情感占比</RouterLink>
        <RouterLink to="/time">一天时间分布</RouterLink>
        <RouterLink to="/heatmap">当年日期分布</RouterLink>
      </nav>
    </div>

    <RouterView />
  </el-card>
</template>

<style scoped>
nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;
  }
}
</style>
