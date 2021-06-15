<template>
  <account-modal :action="this.$options.name"
    >Login with your account and start losing NOW!</account-modal
  >
</template>

<script>
import AccountModal from "../components/AccountModal.vue";
export default {
  name: "Login",
  components: { AccountModal },
};
</script>

<style></style>
