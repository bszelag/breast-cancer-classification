<script>
import { Pie } from 'vue-chartjs'

export default {
  name: 'Accuracy',
  props: ['data'],
  extends: Pie,
  mounted () {
    var keys = []
    var values = []
    var labels = {
      'tp': 'True Positive',
      'fp': 'False Positive',
      'tn': 'True Negative',
      'fn': 'False Negative'
    }
    for (var k in this.data) {
      keys.push(labels[k])
      values.push(this.data[k].toFixed(2))
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
}
</script>
