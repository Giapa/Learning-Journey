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
        <h5>Login with your account and start losing money NOW!</h5>
        <h5>Get addicted and let us gain.</h5>
      </div>
      <login-form></login-form>
    </div>
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";
export default {
  components: { LoginForm },
};
</script>

<style></style>
