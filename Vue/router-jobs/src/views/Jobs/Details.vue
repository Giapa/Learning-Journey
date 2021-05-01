<template>
  <div v-if="job">
    <h1>Job details</h1>
    <h2>{{ job.title }}</h2>
    <p>{{ job.details }}</p>
  </div>
  <div v-else>
    <h1>Loading details</h1>
  </div>
</template>

<script>
export default {
  props: ["id"],
  data() {
    return {
      job: null,
    };
  },
  mounted() {
    fetch(`http://localhost:3000/jobs/${this.id}`)
      .then((res) => res.json())
      .then((data) => (this.job = data))
      .catch((err) => console.log(err.message));
  },
};
</script>

<style></style>
