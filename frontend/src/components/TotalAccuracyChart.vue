<script>
  import { Scatter } from 'vue-chartjs'

  export default {
    name: 'TotalAccuracyChart',
    props: ['data'],
    data () {
      return {
        a: []
      }
    },
    extends: Scatter,
    methods: {
      prepareTotalAccuracyChart: function () {
        var values = []
        var labels = {
          'tp': 'True Positive',
          'fp': 'False Positive',
          'tn': 'True Negative',
          'fn': 'False Negative'
        }
        for (var k in this.a) {
          values.push({x: labels[k], y: this.a[k].toFixed()})
        }
        this.renderChart({
          datasets: [{
            label: 'Total Accuracy',
            data: values
          }],
        }, {
          scales: {
            xAxes: [{
              type: 'linear',
              position: 'bottom'
            }]
          }
        })
      }
    },
    mounted () {
      this.a = this.data
      this.prepareTotalAccuracyChart()
    },
    watch: {
      data: function () {
        this.a = this.data
        this.prepareTotalAccuracyChart()
      }
    }
  }
</script>
