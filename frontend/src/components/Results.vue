<template>
  <b-card v-if="results!=='-'" header="Results" header-bg-variant="info" header-text-variant="white" class="card">
    <div>
      <div v-if="results['accuracy'] !== null" class="results-part">
        <h5>Accuracy (%)</h5>
        <div class="d-flex justify-content-center">
          <accuracy :data="results['accuracy']"></accuracy>
        </div>
      </div>
      <div class="results-part">
        <h5>Additional evaluation measures</h5>
        <div class="d-flex justify-content-around">
          <div v-for="(m, index) in measurements" v-bind:key="index">
            <h6 class="measure-name">{{ index }}</h6>
            <h6 class="measure">{{m.toFixed(3)}}</h6>
          </div>
        </div>
      </div>
      <div class="results-part" v-if="results['options'] !== undefined">
        <h5>Options</h5>
        {{ results['options'] }}
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
      },
      measurements: {
        ERR: 0,
        ACC: 0,
        SN: 0,
        SP: 0,
        PREC: 0,
        FPR: 0,
        F1: 0,
        MCC: 0
      }
    }
  },
  methods: {
    countMeasurements: function () {
      let PN = this.results['accuracy']['tp'] + this.results['accuracy']['tn'] +
        this.results['accuracy']['fp'] + this.results['accuracy']['fn']
      this.measurements.ACC = (this.results['accuracy']['tp'] + this.results['accuracy']['tn']) / PN
      this.measurements.ERR = (this.results['accuracy']['fp'] + this.results['accuracy']['fn']) / PN
      this.measurements.SN = this.results['accuracy']['tp'] /
        (this.results['accuracy']['tp'] + this.results['accuracy']['fn'])
      this.measurements.SP = this.results['accuracy']['tn'] /
        (this.results['accuracy']['tn'] + this.results['accuracy']['fn'])
      this.measurements.PREC = this.results['accuracy']['tp'] /
        (this.results['accuracy']['tp'] + this.results['accuracy']['fp'])
      this.measurements.FPR = 1 - this.measurements.SP
      this.measurements.F1 = (2 * this.measurements.PREC * this.measurements.SN) /
        (this.measurements.PREC + this.measurements.SN)
      this.measurements.MCC = (this.results['accuracy']['tp'] * this.results['accuracy']['tn'] -
        this.results['accuracy']['fp'] * this.results['accuracy']['fn']) /
        (Math.sqrt(
          (this.results['accuracy']['tp'] + this.results['accuracy']['fp']) *
          (this.results['accuracy']['tp'] + this.results['accuracy']['fn']) *
          (this.results['accuracy']['tn'] + this.results['accuracy']['fp']) *
          (this.results['accuracy']['tn'] + this.results['accuracy']['fn'])
        ))
      console.log(this.measurements)
    }
  },
  mounted: function () {
    this.countMeasurements()
  },
  watch: {
    results: function () {
      this.countMeasurements()
      console.log('watch')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.results-part {
  margin-bottom: 30px;
}
.measure {
  margin: 0px 5px;
}
.measure-name {
  font-weight: bold;
}
h5 {
  margin: 20px 0px;
}
</style>
