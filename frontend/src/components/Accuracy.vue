<script>
import { Pie } from 'vue-chartjs'

export default {
  name: 'Accuracy',
  props: ['data', 'prep'],
  data () {
    return {
      acc: null
    }
  },
  extends: Pie,
  methods: {
    prepareAccuracyChart: function () {
      if (this.prep) {
        this.acc = []
        for (var a in this.data) {
          this.acc.push({
            'fn': this.data[a].fn,
            'tp': this.data[a].tp,
            'fp': this.data[a].fp,
            'tn': this.data[a].tn
          })
        }
        console.log('ACC = ' + this.acc)
      }
      var keys = []
      var values = []
      var labels = {
        'tp': 'True Positive',
        'fp': 'False Positive',
        'tn': 'True Negative',
        'fn': 'False Negative'
      }
      for (var k in this.acc) {
        keys.push(labels[k])
        values.push(this.acc[k].toFixed(2))
      }
      this.renderChart({
        datasets: [{
          data: values,
          backgroundColor: [
            '#FFA80B',
            '#B614CC',
            '#3F58CC',
            '#4F993D'
          ]
        }],
        labels: keys
      })
    }
  },
  mounted () {
    this.acc = this.data
    this.prepareAccuracyChart()
  },
  watch: {
    data: function () {
      this.acc = this.data
      this.prepareAccuracyChart()
    }
  }
}
</script>
