<template>
  <div class="home">
    <h1>Home</h1>
    <PostList v-if="showPosts" :posts="posts" />
    <button @click="showPosts = !showPosts">Toggle posts</button>
  </div>
</template>

<script>
import PostList from "../components/PostList.vue";
import { ref } from "@vue/reactivity";

export default {
  name: "Home",
  components: { PostList },
  setup() {
    const posts = ref([
      {
        title: "Welcome to the blog",
        body:
          "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias aut, repellat ipsum facere voluptate dicta obcaecati deserunt nobis suscipit eaque?",
        id: 1,
      },
      {
        title: "top 5 css tips",
        body:
          "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias aut, repellat ipsum facere voluptate dicta obcaecati deserunt nobis suscipit eaque?",
        id: 2,
      },
    ]);
    const showPosts = ref(true);
    return { posts, showPosts };
  },
};
</script>
