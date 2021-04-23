<template>
  <p>Score is: {{ score }} ms</p>
  <p>Your rank is: {{ rank }}</p>
</template>

<script>
export default {
  props: ["score"],
  data() {
    return {
      rank: null,
    };
  },
  mounted() {
    if (this.score < 250) {
      this.rank = "How is that possible";
    } else if (this.score < 400) {
      this.rank = "Rapid reflexes";
    } else {
      this.rank = "Too slow";
    }
  },
};
</script>

<style>
.rank {
  font-size: 1.4rem;
  color: #0faf87;
  font-weight: bold;
}
</style>
