<template>
  <div :class="this.getNumbers.length > 0 ? 'pointer-events-none' : ''">
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
              cursor-pointer
            "
          >
            <nav-item
              v-for="item in filteredMenuItems"
              :key="item.name"
              :url="item.url"
            >
              {{ item.name }}
            </nav-item>
            <li>
              <a
                class="
                  lg:p-4
                  py-1
                  px-0
                  block
                  border-b-2 border-transparent
                  text-lg
                "
                v-if="isLoggedIn"
              >
                {{ currentUser }}
              </a>
            </li>
            <li>
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
                v-if="isLoggedIn"
                @click="logout"
              >
                Logout
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
import NavItem from "./NavItem.vue";
import firebase from "firebase";
import { mapGetters } from "vuex";
export default {
  components: { NavItem },
  data() {
    return {
      isLoggedIn: false,
      currentUser: false,
      menuItems: [
        { name: "Home", url: "/" },
        { name: "Live Draw", url: "/draw" },
        { name: "Login", url: "/login" },
        { name: "Register", url: "/register" },
      ],
    };
  },
  created() {
    if (firebase.auth().currentUser) {
      this.isLoggedIn = true;
      this.currentUser = firebase.auth().currentUser.email;
    }
  },
  methods: {
    logout() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$router.push("/").catch(() => {});
        });
    },
  },
  computed: {
    ...mapGetters(["getNumbers"]),
    filteredMenuItems() {
      if (this.isLoggedIn) {
        return this.menuItems.slice(0, 2);
      }
      return this.menuItems;
    },
  },
};
</script>

<style></style>
