<template>
  <div class="w-1/3 h-1/2 m-5 flex flex-wrap shadow-2xl">
    <div class="rounded-l-lg w-2/5 bg-white p-2 flex items-center flex-col">
      <img
        class="rounded-full h-36 w-36 m-2"
        src="https://www.fillmurray.com/640/360"
        alt="Fill murray"
      />
      <span class="font-bold text-gray-700">Play balance</span>
      <div class="font-bold text-4xl m-2 text-gray-700">&euro;156,00</div>
      <a
        role="button"
        class="bg-green-lime hover:bg-green-600 text-white font-bold text-sm p-3 border rounded-lg w-36 text-center"
      >
        Deposit
      </a>
      <div class="border-t m-3 border-gray-500 w-44" />
      <span class="font-bold text-gray-600">Available to withdraw</span>
      <div class="font-bold text-2xl m-2 text-gray-700">&euro;156,00</div>
      <a
        role="button"
        class=" bg-white hover:bg-gray-300 text-black font-bold text-sm p-3 border-2 border-black rounded-lg w-36 text-center mb-2"
      >
        Withdraw
      </a>
    </div>
    <div class="flex-grow flex flex-col bg-gray-100 rounded-r-lg p-2">
      <div class="flex">
        <span class="flex-grow w-4/6">Bonus</span>
        <span class="flex-grow">Promotions</span>
      </div>
      <div class="flex"></div>
      <div class="flex"></div>
      <div class="flex"></div>
      <div class="flex"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    primary: {
      type: Boolean,
      required: true,
    },
  },
};
</script>

<style>
hr {
  border: 0;
  clear: both;
  display: block;
  width: 96%;
  background-color: #ffff00;
  height: 1px;
}
</style>
