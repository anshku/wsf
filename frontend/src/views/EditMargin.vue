<template>
  <div class="container col-4">
    <form @submit.prevent="handleSubmit">
      <div class="mb-3">
        <label for="margin" class="form-label"
          >New Margin (between 0 and 1.0)</label
        >
        <input
          v-model="margin"
          type="number"
          class="form-control"
          id="margin"
          step="0.1"
          min="0"
          max="1.0"
        />
      </div>
      <div class="d-grid gap-2 col-6 mx-auto mt-4">
        <button type="submit" class="btn btn-primary">Edit</button>
      </div>
    </form>
  </div>
</template>

<script>
import getSinglePlayer from "../composables/getSinglePlayer.js";
import updateMargin from "../composables/updateMargin.js";

export default {
  props: ["id"],
  data() {
    return {
      margin: "",
    };
  },
  mounted() {
    getSinglePlayer(this.id)
      .then(({ data }) => {
        this.margin = data.margin;
      })
      .catch((error) => {
        console.log(error); // we can use toast container to show errors
      });
  },
  methods: {
    handleSubmit() {
      updateMargin(this.id, this.margin)
        .then((res) => {
          console.log(res);
          this.$router.push("/");
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style></style>
