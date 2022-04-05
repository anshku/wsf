<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Margin</th>
          <th scope="col">Odds</th>
          <th scope="col">Position</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in players" :key="player.id">
          <td>{{ player.id }}</td>
          <td>
            <router-link
              :to="{ name: 'EditMargin', params: { id: player.id } }"
            >
              {{ player.name }}
            </router-link>
          </td>
          <td>{{ player.margin }}</td>
          <td>{{ player.odds }}</td>
          <td>{{ player.position }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: ["players"],
};
</script>

<style></style>
