<template>
  <b-table hover :items="items" :fields="fields" head-variant="light">
    <template slot="more" slot-scope="data">
      <button size="sm" class="more" @click.stop="data.toggleDetails"><font-awesome-icon :icon="more" /></button>
    </template>
    <template slot="row-details" slot-scope="data">
      <Results :results="data['item']"></Results>
      <button class="hide" @click="data.toggleDetails"><font-awesome-icon class="more" :icon="hide" /></button>
    </template>
  </b-table>
</template>

<script>
import FontAwesomeIcon from '../../node_modules/@fortawesome/vue-fontawesome'
import { faChevronDown, faChevronUp } from '../../node_modules/@fortawesome/fontawesome-free-solid'
import Results from './Results.vue'

export default {
  name: 'History',
  props: ['samples'],
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
      items: [],
      fields: [
        {key: 'time.$date', sortable: true, formatter: (value, key, item) => { return (new Date(value)).toLocaleString() }, label: 'Date (UTC)'},
        {key: 'classifier_info._id', label: 'Algorithm', sortable: true},
        {key: 'classifier_info.train_file_size', label: 'Train File Size', sortable: true},
        {key: 'samples', label: 'Number of Samples', sortable: true},
        {key: 'classifier_info.training_time', label: 'Training Time', sortable: true},
        {key: 'more'}
      ]
    }
  },
  mounted: function () {
    this.items = this.samples
  },
  watch: {
    samples: function () {
      this.items = this.samples
      console.log('watch')
    }
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
