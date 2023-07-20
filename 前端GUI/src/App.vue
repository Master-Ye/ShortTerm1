<script setup lang="ts">
import axios from "axios";

import { ref } from "vue";
const input = ref("");
const temp = ref("");
const img = ref("");

const emotion = (text: string) => {
  console.log(text);
  axios
    .post(
      "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.f068641877cebd1ce66174ed11431fba.2592000.1691293336.282335-35824863",
      {
        text: text,
      }
    )
    .then((res) => {
      console.log(res);
      dialogTableVisible.value = true;
      confidence.value = res.data.items[0].confidence;
      positive_prob.value = res.data.items[0].positive_prob;
      negative_prob.value = res.data.items[0].negative_prob;
      sentiment.value = res.data.items[0].sentiment;
    });
};
const loading = ref(false);
const dialogTableVisible = ref(false);
const search = async (type: number) => {
  loading.value = true;
  await axios.post("http://localhost:3300/search?key=" + input.value).then((res) => {
    console.log(res);
    temp.value = res.data.data.list[0].songid;
  });
  await axios
    .post(
      "http://localhost:3300/comment?id=" + temp.value + "&type=" + type + "&pageSize=50"
    )
    .then((res) => {
      console.log(res);
      tableData.value = res.data.data.comment.commentlist;
      loading.value = false;
    });
};
const emo = ["消极", "中性", "积极"];
const tableData = ref([]);
const show = () => {
  ifshow.value = !ifshow.value;
};
const ifcloudshow = ref(true);
const showcloud = () => {
  ifcloudshow.value = !ifcloudshow.value;
};
const confidence = ref(0);
const positive_prob = ref(0);
const negative_prob = ref(0);
const sentiment = ref(0);
const ifshow = ref(true);
const loading1 = ref(false);
const upload = () => {
  const formData = new FormData();
  loading1.value = true;
  formData.append("id", temp.value);
  axios
    .post("http://localhost:5000/cloud", formData, {
      responseType: "blob",
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((res) => {
      console.log(res);
      img.value = window.URL.createObjectURL(res.data);
      loading1.value = false;
    });
};
</script>

<template>
  <div>
    <el-input v-model="input" placeholder="请输入歌名" style="display: inline-block" />
    <el-button type="primary" @click="search(0)" style="display: inline-block"
      >获取新评10条</el-button
    >
    <el-button type="primary" @click="search(1)" style="display: inline-block"
      >获取热评50条</el-button
    >
    <el-button type="primary" @click="upload()" v-loading="loading1"
      >获取热评词云</el-button
    >
    <el-button type="info" @click="show()">展开/隐藏评论</el-button>
    <el-button type="info" @click="showcloud()">展开/隐藏词云</el-button>
    <el-table :data="tableData" style="width: 100%" v-loading="loading" v-show="ifshow">
      <el-table-column prop="nick" label="  ID" width="200" />
      <el-table-column prop="rootcommentcontent" label="评论" width="700" />
      <el-table-column fixed="right" label="Operations" width="120">
        <template #default="scope">
          <el-button
            link
            type="primary"
            size="small"
            @click="emotion(scope.row.rootcommentcontent)"
            >获取情感</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <img
      :src="img"
      style="display: block; position: relative; left: 100px"
      v-show="ifcloudshow"
    />
    <el-dialog v-model="dialogTableVisible" title="情感倾向分析">
      <h3>积极概率:{{ positive_prob }}</h3>
      <h3>消极概率:{{ negative_prob }}</h3>
      <h3>置信度:{{ confidence }}</h3>
      <h3>总评:{{ emo[sentiment] }}</h3>
    </el-dialog>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
