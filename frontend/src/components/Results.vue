<template>
  <b-card v-if="results!=='-'" header="Results" header-bg-variant="info" header-text-variant="white" class="card">
    <div>
      <div v-if="results['accuracy'] !== null" class="accuracy">
        <h5>Accuracy (%)</h5>
        <div class="d-flex justify-content-center">
          <accuracy :data="results['accuracy']"></accuracy>
        </div>
      </div>
      <h5>Results</h5>
      <div class="d-flex justify-content-around flex-wrap">
        <div v-for="(k, v) in results['predicted_values']" v-bind:key="v" class="p-3">
          <h6>{{ v }}</h6>
          <b-badge pill :variant="badgeType[k]"> {{ badgeText[k] }} </b-badge>
        </div>
      </div>
    </div>
  </b-card>
</template>

<script>
import Accuracy from './Accuracy.vue'
export default {
  name: 'Results',
  props: ['results'],
  components: {
    Accuracy
  },
  data () {
    return {
      badgeType: {
        0: 'success',
        1: 'danger'
      },
      badgeText: {
        0: 'Bening',
        1: 'Malignant'
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.accuracy {
  margin-bottom: 30px;
}
</style>
