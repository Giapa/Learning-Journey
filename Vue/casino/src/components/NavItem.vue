<template>
  <li>
    <router-link :to="url">
      <a
        class="
          lg:p-4
          py-1
          px-0
          block
          border-b-2 border-transparent
          hover:border-black
          text-lg
        "
      >
        <slot></slot>
      </a>
    </router-link>
  </li>
</template>

<script>
export default {
  props: ["url"],
};
</script>

<style></style>
