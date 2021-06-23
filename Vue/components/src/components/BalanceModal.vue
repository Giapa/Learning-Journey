<template>
  <div
    class="m-5 xl:w-1/3 w-2/3 flex sm:flex-col md:flex-row flex-wrap shadow-2xl"
  >
    <div
      class="h-full w-full xl:w-1/3 flex-grow-2 xl:rounded-l-lg xl:rounded-t-none rounded-t-lg bg-white p-4 flex items-center flex-col"
    >
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
      <div class="border-t my-3 border-gray-500 sm:w-36" />
      <span class="font-bold text-gray-600 text-center"
        >Available to withdraw</span
      >
      <div class="font-bold text-2xl m-2 text-gray-700">&euro;156,00</div>
      <a
        role="button"
        class=" bg-white hover:bg-gray-500 hover:text-white text-black font-bold text-sm p-3 border-2 border-gray-500 rounded-lg w-36 text-center mb-2"
      >
        Withdraw
      </a>
    </div>
    <div
      class="flex-grow flex flex-col bg-gray-100 xl:rounded-r-lg xl:rounded-b-none rounded-b-lg p-2"
    >
      <div class="flex">
        <span class="flex-grow w-3/6 font-semibold text-gray-600">Bonus</span>
        <span class="flex-grow font-semibold text-gray-600">Promotions</span>
      </div>
      <div class="flex my-4">
        <div class="flex-grow flex w-3/6 flex-col sm:flex-row">
          <img
            class="rounded-lg w-20 h-12"
            src="https://www.fillmurray.com/640/360"
            alt="Fill murray"
          />
          <div class="font-bold text-xl m-2 text-gray-600">&euro;156,00</div>
        </div>
        <div class="flex-grow">
          <div
            class="flex text-center pb-5 mt-3 shadow-md bg-gradient-to-r from-blue-500 to-green-400 rounded-full text-white font-sans font-semibold text-sm btn-primary w-24 h-4"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 ml-1 "
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
            Available
          </div>
        </div>
      </div>
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
