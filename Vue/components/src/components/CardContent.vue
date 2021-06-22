<template>
  <div>
    <div>
      <h2 class="text-gray-800 text-3xl font-semibold mb-5">
        <slot></slot>
      </h2>
      <p class="m-2 p-3 text-gray-600">
        <slot name="text"></slot>
      </p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
