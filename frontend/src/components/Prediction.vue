<template>
  <b-container class="bg-light container-class">
    <div class="d-flex justify-content-center">
      <b-card-group deck>
        <b-card header="Classification" header-bg-variant="info" header-text-variant="white" class="card">
          <b-form @submit="onSubmit" @reset="onReset" class="form">
            <b-form-group class="form-group" label="Classification" label-for="classification" description="Choose classification algorithm">
              <b-form-radio-group required id="radios" v-model="form.classification" :options="classificationOptions">
              </b-form-radio-group>
            </b-form-group>
            <b-form-group class="form-group" label="Data" label-for="file" description="Select data">
              <b-form-file ref="fileinput" required v-model="form.file" :state="Boolean(form.file)" placeholder="Choose a file..."></b-form-file>
              <div class="mt-3">Selected file: {{form.file && form.file.name}}</div>
            </b-form-group>
            <b-form-group class="form-group" label="Labels" label-for="target" description="Are there any labels in your data?">
              <b-form-radio-group required id="radios-targets" v-model="form.target" :options="targetOptions">
              </b-form-radio-group>
            </b-form-group>
            <b-button type="submit" variant="success">Classify</b-button>
            <b-button type="reset" variant="secondary">Reset</b-button>
          </b-form>
        </b-card>
        <Results :results="results"></Results>
      </b-card-group>
    </div>
  </b-container>
</template>

<script>
import Results from './Results.vue'

export default {
  name: 'Prediction',
  components: {
    Results
  },
  data () {
    return {
      form: {
        classification: '',
        file: null,
        target: ''
      },
      classificationOptions: [
        {text: 'Naive Bayes', value: 'bayes'},
        {text: 'Decision Tree', value: 'tree'},
        {text: 'SVM', value: 'svm'}
      ],
      targetOptions: [
        {text: 'Data without labels', value: 'false'},
        {text: 'Data with labels', value: 'true'}
      ],
      results: '-'
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
      this.form.target = ''
      this.results = '-'
      this.$refs.fileinput.reset()
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    submit: async function () {
      let endpoint = this.form.classification + '/predict'
      let formData = new FormData()
      formData.append('file', this.form.file)
      formData.append('with_target', this.form.target)
      try {
        const results = await this.$http.post(endpoint, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log(results)
        if (results.statusText === 'OK') {
          this.results = results.data
          alert('Classification has finished!')
        }
      } catch (err) {
        console.log(err)
        alert('Error: ' + err)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card{
    margin-top: 50px;
  }
  .form-group {
    margin-bottom: 25px;
  }
  .result {
    margin: 5px 20px;
  }
</style>
