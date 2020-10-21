<template>
  <v-app>
    <v-app-bar app dark>
      <div class="d-flex align-center mr-2">
        Lucky Fox Farms
      </div>

      <v-btn to="/horses" text>
        Horses
      </v-btn>

      <v-btn to="/addLesson" text>
        Add Lesson
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "app",
};
</script>
