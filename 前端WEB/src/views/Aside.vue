<template>
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo fixed left-0 top-0 h-full"
    background-color="#545c64"
    @open="handleOpen"
    @close="handleClose"
  >
    <el-menu-item index="1">
      <el-icon><setting /></el-icon>
      <span>《花海》评论数据可视化</span>
    </el-menu-item>

    <el-menu-item index="2">
      <el-icon><setting /></el-icon>
      <span>手动搜索歌名可视化</span>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
import { Document, Menu as IconMenu, Location, Setting } from "@element-plus/icons-vue";
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>
