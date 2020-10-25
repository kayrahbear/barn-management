<template>
  <div class="main-container">
    <v-row v-if="currentHorse">
      <v-col :cols="2"></v-col>
      <v-col :cols="4">
        <v-img
          :src="currentHorse.horse_img"
          height="650px"
          position="top"
        ></v-img>
      </v-col>
      <v-col :cols="4">
        <div class="text-h2">
          {{ currentHorse.short_name }}
        </div>
        <hr />
        <div class="text-h4">
          {{ currentHorse.breed }} {{ currentHorse.sex }} |
          {{ getAge(currentHorse.birth_year) }} years old
        </div>
        <div class="text-subtitle-2 font-weight-light">
          Born {{ currentHorse.birth_year }}
        </div>
        <div class="text-body-1 my-4">
          <span class="font-weight-bold">Owner:</span> {{ currentHorse.owner }}
        </div>
        <v-tabs  color="brown" v-model="tab" align-with-title :method="splitFeed(horseFeed, horseSupplements)">
          <v-tabs-slider color="brown"></v-tabs-slider>
          <v-tab
            ><v-icon dark right class="mx-1"> mdi-white-balance-sunny </v-icon>
            AM Feed</v-tab
          >
          <v-tab
            ><v-icon dark right class="mx-1"> mdi-weather-night </v-icon> PM
            Feed</v-tab
          >
          <v-tab
            ><v-icon dark right class="mx-1"> mdi-flower </v-icon> Turnout
            Schedule</v-tab
          >
        </v-tabs>

        <!-- <v-btn color="brown darken-3 white--text mx-1">
          <v-icon dark right class="mx-1"> mdi-white-balance-sunny </v-icon>
          AM Feed
        </v-btn>
        <v-btn color="brown darken-3 white--text mx-1">
          <v-icon dark right class="mx-1"> mdi-weather-night </v-icon>
          PM Feed
        </v-btn>
        <v-btn color="brown darken-3 white--text mx-1">
          <v-icon dark right class="mx-1"> mdi-flower </v-icon>
          Turnout Schedule
        </v-btn> -->
      </v-col>
    </v-row>
    <v-row>
      <v-col :cols="6"> </v-col>
    </v-row>
  </div>
</template>

<script>
import SingleHorseDataService from "../services/SingleHorseDataService";

export default {
  name: "horse",
  data() {
    return {
      currentHorse: null,
      horseFeed: null,
      horseSupplements: [],
      turnouts: [],
      amFeed: null,
      pmFeed: null,
      tab: null,
    };
  },
  methods: {
    getHorse(id) {
      SingleHorseDataService.getHorse(id)
        .then((response) => {
          this.currentHorse = response.data;
          console.log("I WENT SOMEWHERE", response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getFeed(id) {
      SingleHorseDataService.getFeed(id)
        .then((response) => {
          this.horseFeed = response.data.results;
          console.log("I WENT FOR FEWDS", response.data.results);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getSupplements(id) {
      SingleHorseDataService.getSupps(id)
        .then((response) => {
          this.horseSupplements = response.data.results;
          console.log("I WENT FOR MEDICINE", response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getAge(birthday) {
      var birthYear = birthday;
      var date = new Date();
      var currentYear = date.getFullYear();
      var age = currentYear - birthYear;

      if (age >= 1) {
        return age;
      } else {
        return birthYear;
      }
    },
    splitFeed(feeds, supps) {
    var feed = feeds[0];
    var suppList = supps;
    var amSups = [];
    var pmSups = [];
    for (let index = 0; index < suppList.length; index++) {
        const supp = suppList[index];
        if (supp.supp_time.includes("AM")) {
            amSups.push(supp)
        }
        if(supp.supp_time.includes("PM")) {
            pmSups.push(supp)
        }    
    }
    
    var amFeed = feed;
    amFeed["amSups"] = amSups;
    var pmFeed = feed;
    pmFeed["pmSups"] = pmSups;

    this.amFeed = amFeed;
    this.pmFeed = pmFeed;

    },
  },
  mounted() {
    this.getHorse(this.$route.params.id);
    this.getFeed(this.$route.params.id);
    this.getSupplements(this.$route.params.id);
  },
};
</script>