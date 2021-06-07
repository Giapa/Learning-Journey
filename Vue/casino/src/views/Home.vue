<template>
  <div>
    <h1
      class="
        text-4xl
        sm:text-6xl
        lg:text-7xl
        leading-none
        font-extrabold
        tracking-tight
        text-gray-900
        mt-10
        mb-5
        sm:mt-14 sm:mb-10
        inline-flex
        items-center
      "
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-12 w-20 inline-block"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
        />
      </svg>
      Money Loss.
    </h1>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-5
        sm:mb-5
        text-center
      "
    >
      Your pain is our gain. Play to lose.
    </p>
    <a
      class="
        w-full
        sm:w-auto
        flex-none
        bg-gray-900
        hover:bg-gray-700
        text-white text-lg
        leading-6
        font-semibold
        py-3
        px-6
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
      href=""
      >Start losing</a
    >
    <h1 class="my-10">
      More than 100.000.000 people have lost their entire property. Don't miss
      out on the feeling.
    </h1>
    <p
      class="
        text-lg
        sm:text-2xl sm:leading-10
        font-medium
        mb-2
        sm:mb-2
        text-center
      "
    >
      Our users say:
    </p>
    <div class="justify-center items-stretch flex space-x-20">
      <user-card v-for="user in users" :key="user.name">
        <template v-slot:name>{{ user.name }}</template>
        <q> {{ user.testimony }} </q>
        <template v-slot:price>{{ user.lost }} &#36;</template>
      </user-card>
    </div>
  </div>
</template>

<script>
import UserCard from "../components/UserCard.vue";
export default {
  name: "Home",
  components: { UserCard },
  data() {
    return {
      users: [
        {
          name: "Gregory Giapa",
          testimony: "I lost everything to my gabling addiction.",
          lost: "40000",
        },
        {
          name: "Linus TechTips",
          testimony:
            "The tips they gave me weren't enought to keep my wife from leaving me.",
          lost: "500204",
        },
        {
          name: "Richard Stallman",
          testimony: "I lost all the GNU money to this propriatary web app.",
          lost: "100223421",
        },
      ],
    };
  },
};
</script>
