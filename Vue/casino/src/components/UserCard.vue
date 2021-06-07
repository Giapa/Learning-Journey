<template>
  <div class="max-w-xs mx-10 rounded overflow-hidden shadow-lg my-2">
    <img
      class="w-full"
      src="https://www.fillmurray.com/640/360"
      alt="Sunset in the mountains"
    />
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2"><slot name="name"></slot></div>
      <p class="text-grey-darker text-base">
        <slot></slot>
      </p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
