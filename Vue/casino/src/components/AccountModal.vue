<template>
  <div class="flex items-center justify-center mt-48">
    <div
      class="
        bg-gray-500
        text-white
        font-bold
        rounded-lg
        border
        shadow-lg
        p-10
        grid grid-cols-2
        gap-5
        divide-x
      "
    >
      <div>
        <h1
          class="
            text-2xl
            sm:text-2xl
            lg:text-4xl
            leading-none
            font-extrabold
            tracking-tight
            text-gray-900
            mt-5
            mb-5
            sm:mt-10 sm:mb-5
            inline-flex
            items-center
          "
        >
          Welcome to Money Loss
        </h1>
        <h5><slot></slot></h5>
        <h5>Get addicted and let us gain.</h5>
      </div>
      <account-form :action="action"></account-form>
    </div>
  </div>
</template>

<script>
import AccountForm from "./AccountForm.vue";
export default {
  props: ["action"],
  components: { AccountForm },
};
</script>

<style></style>
