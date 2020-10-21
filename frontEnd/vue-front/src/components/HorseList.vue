<template>
  <div class="card-container">
    <v-row>
    <v-card
      class="mx-auto"
      max-width="400"
      v-for="horse in horses" :key="horse.id"
    >
      <v-img
        class="white--text align-end"
        height="200px"
        :src="horse.horseImage"
      >
        <v-card-title>{{ horse.shortName }}</v-card-title>
      </v-img>

      <v-card-subtitle class="pb-0">
        Stall #:
      </v-card-subtitle>

      <v-card-text class="text--primary">
        <div>{{ horse.breed }} {{ horse.sex }}</div>

        <div>Born {{ horse.birthYear }}</div>
      </v-card-text>

      <v-card-actions>
        <v-btn
          color="orange"
          text
        >
          Share
        </v-btn>

        <v-btn
          color="orange"
          text
        >
          Explore
        </v-btn>
      </v-card-actions>
    </v-card>
    </v-row>
  </div>
</template>

<script>
import HorseDataService from "../services/HorseDataService";
export default {
  name: "horses-list",
  data() {
    return {
      horses: [],
    };
  },
  methods: {
    retrieveHorses() {
      HorseDataService.getAll()
        .then((response) => {
          this.horses = response.data.results.map(this.getDisplayHorse);
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveHorses();
    },

    searchShortName() {
      HorseDataService.findByShortName(this.shortName)
        .then((response) => {
          this.horses = response.data.results.map(this.getDisplayHorse);
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    // editTutorial(id) {
    //   this.$router.push({ name: "tutorial-details", params: { id: id } });
    // },

    // deleteTutorial(id) {
    //   TutorialDataService.delete(id)
    //     .then(() => {
    //       this.refreshList();
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },

    getDisplayHorse(horse) {
      return {
        id: horse.id,
        shortName: horse.short_name,
        breed: horse.breed,
        birthYear: horse.birth_year,
        horseImage: horse.horse_img,
        sex: horse.sex,
      };
    },
  },
  mounted() {
    this.retrieveHorses();
  },
};
</script>

<style>
.list {
  max-width: 750px;
}
</style>