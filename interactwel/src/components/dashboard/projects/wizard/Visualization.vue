<template>
  <div>
    <b-row class="my-3">
      <b-col>
        <h6>
          Adaptation Plan {{ $route.params.planId }}
        </h6>
      </b-col>
      <b-col>
        <b-button
          id="feedback-btn"
          variant="next"
          size="sm"
          @click="showFeedback"
        >Provide Feedback
        </b-button>
      </b-col>
    </b-row>
    <router-view/>
  </div>
</template>
<script>
import EventBus from '../../../../event-bus';

export default {
  name: 'Visualization',
  props: {},
  data() {
    return {};
  },
  watch: {},
  mounted() {

  },
  methods: {
    showFeedback() {
      EventBus.$emit('SHOW_FEEDBACK_BLOCK', true);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
