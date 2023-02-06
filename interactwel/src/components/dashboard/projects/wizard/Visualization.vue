<template>
  <div>
    <h6 class="mt-3">
      <div class="title">
        <div>Adaptation Plan {{ $route.params.planId }}</div> <div>Feedback</div> 
      </div>
    </h6>
    <router-view />
  </div>
</template>
<script>

export default {
  name: 'Visualization',
  props: {},
  data() {
    return {};
  },
  watch: {},
  mounted() {

  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .title{
    border: 1px solid black;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }
</style>
