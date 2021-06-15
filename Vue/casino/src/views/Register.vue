<template>
  <account-modal :action="this.$options.name"
    >Register a new account and start losing NOW!</account-modal
  >
</template>

<script>
import AccountModal from "../components/AccountModal.vue";

export default {
  name: "Register",
  components: { AccountModal },
};
</script>

<style></style>
