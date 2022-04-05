<template>
  <div>
    <h1>Players List</h1>
    <div v-if="players.length">
      <Table :players="players" />
    </div>
    <div v-else>
      <Spinner />
    </div>
  </div>
</template>

<script>
import Table from "../components/Table.vue";
import Spinner from "../components/Spinner.vue";
import getPlayers from "../composables/getPlayers.js";

export default {
  name: "Players",
  components: { Table, Spinner },
  data() {
    return {
      players: [],
    };
  },
  mounted() {
    getPlayers()
      .then(({ data }) => {
        this.players = data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style></style>
