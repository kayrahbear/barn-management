<template>
  <v-app>
    <v-app-bar app dark class="brown darken-4">
      <div class="d-flex align-center mr-2">
        Lucky Fox Farms
      </div>

      <v-btn to="/horses" text>
        Horses
      </v-btn>

      <v-btn to="/myProfile" text>
        My Profile
      </v-btn>

      <v-btn to="/workingStudents" text>
        Working Students
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
