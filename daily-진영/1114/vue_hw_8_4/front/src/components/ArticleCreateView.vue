<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="goCreate">
      <label for="asdf">제목 :</label>
      <input type="text" id="asdf" v-model="title">
      <label for="fdsa">내용 :</label>
      <input type="text" id="fdsa" v-model="content">
      <input type="submit" value="create">
    </form>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const router = useRouter()

const title = ref('')
const content = ref('')

const goCreate = function() {
  axios({
    method : "post",
    url : 'http://127.0.0.1:8000/api/v1/articles/',
    data : {
      title: title.value,
      content : content.value,
    }
  }).then(() => router.push({
    name:'home'
  })).catch((err) => console.log(err))
}

</script>

<style lang="scss" scoped>

</style>