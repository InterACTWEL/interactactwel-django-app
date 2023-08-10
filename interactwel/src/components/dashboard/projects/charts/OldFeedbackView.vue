<template>
  <div>
    <b-card title="My Feedback">
      <b-card-text>
        <div>
          Feedback Provided DateTime: {{ new Date(feedback.date_modified)| dateFormat('YYYY.MM.DD : HH.mm') }}
        </div>
        <hr>
        <div v-if="feedback.rating != null">
          Which plan do you prefer more? 
          <vue-slider
            :min="1"
            :max="5"
            :value="feedback.rating"
            @input="onRatingChange"
            :start-value="2.5"
            style=":width :200px"
            :label-position="'under'"
            :label="'Action Plan {{ $route.params.planId }}' | 'Business As Usual'"
          />
          <p><b>Action Plan {{ $route.params.planId }}</b>                                             <b>Business As Usual</b>
            </p>
        </div>
        <hr>
        <div>
          
          Question: Do you think the actions and timeframes presented in this plan are feasible?
          <br>
          Answer: {{ feedback.feasibilty==1 ? 'Yes' : 'No' }}
        </div>
        <hr>
        <div
          v-for="feedbackItem in feedback.feedback_answers"
          :key="feedbackItem.id"
        >
          Question: {{ feedbackItem.question }}
          <br>
          Answer: {{ feedbackItem.answer }}
          <hr>
        </div>
        <div v-if="feedback.comments != null">
          Comment: {{ feedback.comments }}
        </div>
        <hr>
        <!-- <div v-if="feedback.rating != null">
          Which plan do you prefer more? 
          <vue-slider
            :min="1"
            :max="5"
            :value="feedback.rating"
            @input="onRatingChange"
            :start-value="2.5"
            style=":width :200px"
            :label-position="'under'"
            :label="'Action Plan {{ $route.params.planId }}' | 'Business As Usual'"
          />
          <p><b>Action Plan {{ $route.params.planId }}</b>----------------------------------------------------------<b>Business As Usual</b>
            </p>
        </div> -->
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import VueSlider from 'vue-slider-component';

export default {
  name: "OldFeedbackView",
  props: {
    feedback: null,
  },
  components: {
    VueSlider,
  },
  methods: {
    onRatingChange(value) {
      this.feedback.rating = value;
    },
  },
};
</script>

<style scoped>

</style>
