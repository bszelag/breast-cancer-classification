<template>
  <b-container class="bg-light statsTable">
    <TotalAccuracy :accuracy="accuracy"></TotalAccuracy>
    <b-form-group class="filter">
      <b-form-checkbox-group v-model="filter" buttons button-variant="outline-info" size="sm">
        <b-form-checkbox value='bayes'>Naive Bayes</b-form-checkbox>
        <b-form-checkbox value='svm'>SVM</b-form-checkbox>
        <b-form-checkbox value='tree'>Decision Tree</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
    <History :samples="samples"></History>
  </b-container>
</template>

<script>
import History from './History.vue'
import TotalAccuracy from './TotalAccuracy.vue'

export default {
  name: 'Statistics',
  data () {
    return {
      samples: [],
      bayes: true,
      svm: true,
      tree: true,
      accuracy: [],
      filter: [],
      filterValues: {
        'bayes': this.$statsBayes + this.$historyEndpoint + '/0',
        'svm': this.$statsSVM + this.$historyEndpoint + '/0',
        'tree': this.$statsTree + this.$historyEndpoint + '/0'
      }
    }
  },
  components: {
    History,
    TotalAccuracy
  },
  methods: {
    getHistory: async function (endpoint) {
      try {
        const response = await this.$http.get(endpoint)
        for (var d in response.data) {
          this.samples.push({
            'accuracy': response.data[d].accuracy,
            'algorithm': response.data[d].classifier_info['_id'],
            'size': response.data[d].classifier_info['train_file_size'],
            'predicted_values': response.data[d].predicted_values,
            'time': response.data[d].time,
            'samples': Object.keys(response.data[d].predicted_values).length,
            'classifier_info': response.data[d].classifier_info
          })
        }
        console.log(this.samples)
      } catch (err) {
        console.log(err)
      }
    },
    getTotalAccuracy: async function (endpoint) {
      try {
        const response = await this.$http.get(endpoint)
        for (var d in response.data) {
          this.accuracy.push({
            'id': response.data[d]['_id'],
            'values': {
              'fn': response.data[d]['fn'] / response.data[d]['total'] * 100,
              'tp': response.data[d]['tp'] / response.data[d]['total'] * 100,
              'tn': response.data[d]['tn'] / response.data[d]['total'] * 100,
              'fp': response.data[d]['fp'] / response.data[d]['total'] * 100
            }
          })
        }
        console.log('stats acc - ' + this.accuracy)
      } catch (err) {
        console.log(err)
      }
    }
  },
  mounted: function () {
    this.getHistory(this.$statsBayes + this.$historyEndpoint + '/0')
    this.getHistory(this.$statsSVM + this.$historyEndpoint + '/0')
    this.getHistory(this.$statsTree + this.$historyEndpoint + '/0')
    this.getTotalAccuracy(this.$statsBayes + this.$accuracyEndpoint)
    this.getTotalAccuracy(this.$statsSVM + this.$accuracyEndpoint)
    this.getTotalAccuracy(this.$statsTree + this.$accuracyEndpoint)
  },
  watch: {
    filter: function () {
      this.samples = []
      for (var f in this.filter) {
        this.getHistory(this.filterValues[this.filter[f]])
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.statsTable {
  padding: 20px;
  margin-top: 25px;
}
.filter {
  margin: 15px 0px;
}
</style>
