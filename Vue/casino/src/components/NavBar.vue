<template>
  <div class="antialias">
    <header
      class="
        lg:px-16
        px-6
        flex flex-wrap
        items-center
        lg:py-0
        py-2
        mx-8
        my-2
        rounded-lg
        bg-green-200 bg-gradient-to-br
        from-green-200
        to-green-300
      "
    >
      <div class="flex-1 flex justify-between items-center">
        <img
          src="https://www.pngrepo.com/png/246918/512/dices-casino.png"
          alt="Dice"
          width="50"
          height="50"
        />
      </div>

      <div class="hidden lg:flex lg:items-center lg:w-auto w-full">
        <nav>
          <ul
            class="
              lg:flex
              items-center
              justify-between
              text-base text-gray-700
              pt-4
              lg:pt-0
            "
          >
            <nav-item v-for="item in menuItems" :key="item">
              {{ item }}
            </nav-item>
          </ul>
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
import NavItem from "./NavItem.vue";

export default {
  components: { NavItem },
  data() {
    return {
      menuItems: ["Home", "Draw", "Login", "Register"],
    };
  },
};
</script>

<style></style>
