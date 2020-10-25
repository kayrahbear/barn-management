<template>
  <div class="card-container">
    <v-row>
    <v-card
      class="mx-auto my-2"
      max-width="400"
      v-for="horse in horses" :key="horse.id"
    >
      <v-img
        class="white--text align-end"
        height="500px"
        position="top"
        :src="horse.horseImage"
      >
      </v-img>
      <v-card-title>{{ horse.shortName }}</v-card-title>
      <v-card-subtitle class="pb-0">
        Stall #:
      </v-card-subtitle>

      <v-card-text class="text--primary">
        <div>{{ horse.breed }} {{ horse.sex }}</div>

        <div>Born {{ horse.birthYear }}</div>
      </v-card-text>

      <v-card-actions>
        <v-btn
          color="brown darken-3 white--text"
          @click="viewHorse(horse.id)"
        >
          <v-icon
            dark
            left
          >
            mdi-horse
          </v-icon>
          View Details 
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

    viewHorse(id) {
      this.$router.push({ name: "horse-details", params: { id: id } });
    },

    getDisplayHorse(horse) {
      return {
        id: horse.horse_id,
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