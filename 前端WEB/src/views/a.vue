<template>
  <div>
    <span> {{ mess }}</span>
    <button @click="dayin()"></button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mess: 111,
    };
  },
  onMounted() {
    console.log("mounted");
    this.mess = 222;
  },
  methods: {
    dayin() {
        this.mess=this.mess+1
    },
    dayin1() {},
  },
};
</script>

<style scoped></style>
