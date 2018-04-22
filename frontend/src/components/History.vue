<template>
  <div>
    <b-table hover :items="samples" :fields="fields" head-variant="light">
      <template slot="more" slot-scope="data">
        <button size="sm" class="more" @click.stop="data.toggleDetails"><font-awesome-icon :icon="more" /></button>
      </template>
      <template slot="row-details" slot-scope="data">
        <Results :results="data['item']"></Results>
        <button class="hide" @click="data.toggleDetails"><font-awesome-icon class="more" :icon="hide" /></button>
      </template>
    </b-table>
  </div>
</template>

<script>
import FontAwesomeIcon from '../../node_modules/@fortawesome/vue-fontawesome'
import { faChevronDown, faChevronUp } from '../../node_modules/@fortawesome/fontawesome-free-solid'
import Results from './Results.vue'

export default {
  name: 'History',
  props: ['hist'],
  components: {
    // eslint-disable-next-line
    FontAwesomeIcon,
    Results
  },
  computed: {
    more () {
      return faChevronDown
    },
    hide () {
      return faChevronUp
    }
  },
  data () {
    return {
      samples: [],
      fields: [
        {key: 'time.$date', sortable: true, formatter: (value, key, item) => { return (new Date(value)).toLocaleString() }, label: 'Date (UTC)'},
        //        {key: 'classifier_info.id', label: 'Algorithm', sortable: true},
        //        {key: 'classifier_info.size', label: 'Size', sortable: true},
        {key: 'accuracy.tp', sortable: true},
        {key: 'more'}
      ]
    }
  },
  mounted: function () {
    for (var d in this.hist) {
      this.samples.push({
        'accuracy': this.hist[d].accuracy,
        'classifier_info': this.hist[d].classifier_info,
        'predicted_values': this.hist[d].predicted_values,
        'time': this.hist[d].time
      })
    }
    console.log('samples = ' + this.samples)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
button.hide, button.more {
  width: 100%;
  background-color: inherit;
  border: 1px solid #e9ecef;
}
button.hide:hover, button.more:hover {
  cursor: pointer;
  color: #17a2b8 !important;
}
</style>
