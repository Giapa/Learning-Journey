<template>
  <div
    id="app"
    class="bg-gray-400 h-screen p-5 items-center flex justify-center"
  >
    <balance-modal :primary="true"></balance-modal>
  </div>
</template>

<script>
import BalanceModal from "./components/BalanceModal.vue";

export default {
  components: { BalanceModal },
  name: "App",
};
</script>

<style></style>
