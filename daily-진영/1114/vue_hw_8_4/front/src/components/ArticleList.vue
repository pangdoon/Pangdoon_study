<template>
  <button @click="goCreate">게시글 생성</button>
  <div v-for="article in store.articles" 
  :key="article.id"
  :article="article">
    <p>{{ article.id }}번 게시글</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles' 
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

const router = useRouter()

const goCreate = function() {
  router.push({
    name:'create'
  })
}
</script>

<style lang="scss" scoped>

</style>