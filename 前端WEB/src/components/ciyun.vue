<script setup>
import img from "../assets/grwordcloud1.png";
import axios from "axios";
const img1 = ref(img);
const input = ref("");
const loading = ref(false);
import { ref } from "vue";
const fileList = ref([]);
const upload = () => {
  const formData = new FormData();
  formData.append("image", fileList.value[0].raw);
  formData.append("text", input.value);
  loading.value = true;
  axios
    .post("http://localhost:5000/process", formData, {
      responseType: "blob",
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((res) => {
      console.log(res);
      img1.value = window.URL.createObjectURL(res.data);
      loading.value = false;
    });
};
</script>

<template>
  <div class="greetings">
    <el-card class="box-card w-130">
      <template #header>
        <div class="card-header">
          <span style="font-size: large">《花海》评论自定义词云</span>
        </div>
      </template>
      <el-input v-model="input" placeholder="输入删除词" />
      <el-upload
        accept=".png,.jpg"
        v-model:file-list="fileList"
        class="upload-demo"
        :auto-upload="false"
        multiple
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        :limit="1"
        :on-exceed="handleExceed"
        v-loading="loading"
      >
        <el-button type="primary">点击上传形状图片，背景白色</el-button>
        <template #tip>
          <div class="el-upload__tip">jpg/png files</div>
        </template>
      </el-upload>
      <el-button type="primary" @click="upload">获取词云图片</el-button>
      <img :src="img1" style="width: 400px; height: 450px" />
    </el-card>
  </div>
</template>

<style scoped></style>
