<template>
  <div class="statistics d-flex justify-content-center">
    <History :hist="stats"></History>
  </div>
</template>

<script>
import History from './History.vue'

export default {
  name: 'Statistics',
  data () {
    return {
      stats: [],
      bayes: true,
      svm: true,
      tree: true,
      accuracy: []
    }
  },
  components: {
    History
  },
  methods: {
    getHistory: async function (endpoint) {
      try {
        const response = await this.$http.get(endpoint)
        this.stats = {...this.stats, ...response.data}
      } catch (err) {
        console.log(err)
      }
    }
  },
  mounted: function () {
    this.getHistory(this.$statsBayesHistory + '/0')
    this.getHistory(this.$statsSVMHistory + '/0')
    this.getHistory(this.$statsTreeHistory + '/0')
    console.log(this.stats)
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.statistics {
  padding: 10px;
  margin: 10px;
}
</style>
