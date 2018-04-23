<template>
  <div class="flex flex-nowrap justify-content-around">
    <div v-for="item in items" v-bind:key="item">
      <accuracy :data="item" prep=True></accuracy>
    </div>
  </div>
</template>

<script>
import Accuracy from './Accuracy.vue'

export default {
  name: 'TotalAccuracy',
  props: ['accuracy'],
  components: {
    Accuracy
  },
  data () {
    return {
      items: []
    }
  },
  mounted: function () {
    this.items = this.accuracy
  },
  watch: {
    accuracy: function () {
      this.items = this.accuracy
      //      for (var a in this.accuracy) {
      //        this.items.push({
      //          'fn': this.accuracy[a].fn,
      //          'tp': this.accuracy[a].tp,
      //          'fp': this.accuracy[a].fp,
      //          'tn': this.accuracy[a].tn
      //        })
      //      }
      console.log(this.items)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
