<template>
  <b-container class="bg-light container-class">
    <div class="d-flex justify-content-center">
      <b-card header="Train new classificator" header-bg-variant="info" header-text-variant="white" class="card">
        <b-form @submit="onSubmit" @reset="onReset" class="form">
          <b-form-group label="Classification" label-for="classification" description="Choose classification algorithm">
            <b-form-radio-group required id="radios" v-model="form.classification" :options="classificationOptions">
            </b-form-radio-group>
          </b-form-group>
          <b-form-group label="Options" label-for="args.options" description="Additional options">
            <div v-if="form.classification === 'bayes'">
              <b-form-radio-group id="bayesOptions" v-model="form.args.options['dist']" :options="distOptions">
              </b-form-radio-group>
              {{ form.args.options ? form.args.options : 'nuuuu' }}
            </div>
            <div v-if="form.classification === 'svm'">svm opt</div>
            <div v-if="form.classification === 'tree'">tree opt</div>
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
  </b-container>
</template>

<script>
export default {
  name: 'Training',
  data () {
    return {
      form: {
        classification: '',
        args: {
          options: {}
        },
        file: null
      },
      classificationOptions: [
        {text: 'Naive Bayes', value: 'bayes'},
        {text: 'Decision Tree', value: 'tree'},
        {text: 'SVM', value: 'svm'}
      ],
      argsOptions: {
        'bayes': {'dist': null},
        'svm': {'kernel': null, 'C': null, 'gamma': null},
        'tree': {'criterion': null, 'min_samples_split': null, 'splitter': null}
      },
      distOptions: [
        {text: 'Gaussian Naive Bayes', value: 'GaussianNB'},
        {text: 'Multinominal Naive Bayes', value: 'MultinominalNB'}
      ],
      kernelOptions: [
        {text: 'Linear', value: 'linear'},
        {text: 'Poly', value: 'poly'},
        {text: 'RBF', value: 'rbf'},
        {text: 'Signoid', value: 'signoid'},
        {text: 'Precomputed', value: 'precomputed'}
      ],
      cOptions: [
        {text: '10', value: 10},
        {text: '100', value: 100},
        {text: '1000', value: 1000}
      ],
      gammaOptions: [
        {text: '0.1', value: 0.1},
        {text: '0.01', value: 0.01},
        {text: '0.001', value: 0.001},
        {text: '0.0001', value: 0.0001}
      ],
      criterionOptions: [
        {text: 'Gini', value: 'gini'},
        {text: 'Entropy', value: 'entropy'}
      ],
      splitterOptions: [
        {text: 'Best', value: 'best'},
        {text: 'Random', value: 'random'}
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
        alert('Error: ' + err)
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
