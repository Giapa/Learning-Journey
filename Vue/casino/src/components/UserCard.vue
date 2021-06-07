<template>
  <div
    class="
      mx-2
      rounded
      overflow-hidden
      my-1
      flex flex-col
      border-solid border-2 border-gray-400
    "
  >
    <img
      class="flex rounded-full p-2"
      src="https://www.fillmurray.com/640/360"
      alt="Sunset in the mountains"
    />
    <div class="mt-2 my-2 flex-1">
      <div class="font-bold text-xl mb-2"><slot name="name"></slot></div>
      <p class="text-grey-darker text-base">
        <slot></slot>
      </p>
      <div
        class="
          mx-24
          sm:w-auto
          flex-none
          bg-gray-900
          hover:bg-gray-700
          text-white text-lg
          leading-6
          font-semibold
          mt-5
          border border-transparent
          rounded-xl
          focus:ring-2
          focus:ring-offset-2
          focus:ring-offset-white
          focus:ring-gray-900
          focus:outline-none
          transition-colors
          duration-200
        "
      >
        Loss:
        <slot name="price"></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
