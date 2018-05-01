<template>
  <div class="d-flex flex-nowrap justify-content-around">
    <div class="w-25 d-line-flex" v-for="(item, index) in items" :key="index">
      {{ classificationOptions[item['id']] + ' (%) ' }}
      <accuracy :data="item['values']"></accuracy>
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
      items: [],
      classificationOptions: {
        'bayes': 'Naive Bayes',
        'tree': 'Decision Tree',
        'svm': 'SVM'
      }
    }
  },
  mounted: function () {
    this.items = this.accuracy
  },
  watch: {
    accuracy: function () {
      this.items = this.accuracy
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
