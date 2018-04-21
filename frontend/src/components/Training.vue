<template>
  <div class="d-flex justify-content-center">
    <b-card header="Train new classificator" header-bg-variant="info" header-text-variant="white" class="card">
      <b-form @submit="onSubmit" @reset="onReset" class="form">
        <b-form-group label="Classification" label-for="classification" description="Choose classification algorithm">
          <b-form-radio-group required id="radios" v-model="form.classification" :options="classificationOptions">
          </b-form-radio-group>
        </b-form-group>
        <b-form-group label="Training data" label-for="file" description="Select training data">
          <b-form-file ref="fileinput" required v-model="form.file" :state="Boolean(form.file)" placeholder="Choose a file..."></b-form-file>
          <div class="mt-3">Selected file: {{form.file && form.file.name}}</div>
        </b-form-group>
        <b-button type="submit" variant="success">Train</b-button>
        <b-button type="reset" variant="secondary">Reset</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'Training',
  data () {
    return {
      form: {
        classification: '',
        file: null
      },
      classificationOptions: [
        {text: 'Naive Bayes', value: 'bayes'},
        {text: 'Decision Tree', value: 'tree'},
        {text: 'SVM', value: 'svm'}
      ]
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      this.submit()
    },
    onReset (evt) {
      evt.preventDefault()
      /* Reset our form values */
      this.form.classification = ''
      this.form.file = null
      this.$refs.fileinput.reset()
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    submit: function () {
      let endpoint = this.form.classification + '/train'
      let formData = new FormData()
      formData.append('file', this.form.file)
      this.$http.post(endpoint, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(function () {
        console.log('success')
        alert('Training data successfully sent')
      }).catch(function (err) {
        console.log('error' + err)
      })
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card{
  margin-top: 50px;
}
</style>
