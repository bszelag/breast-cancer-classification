<template>
  <b-container class="bg-light container-class">
    <div class="d-flex justify-content-center">
      <b-card header="Train new classificator" header-bg-variant="info" header-text-variant="white" class="card">
        <b-form @submit="onSubmit" @reset="onReset" class="form">
          <b-form-group label="Classification" label-for="classification" description="Choose classification algorithm">
            <b-form-radio-group required id="radios" v-model="form.classification" :options="classificationOptions" @change="algChanged">
            </b-form-radio-group>
          </b-form-group>
            <div v-if="form.classification === 'bayes'">
              <b-form-group label="Distribution" description="Type of distribution used in Naive Bayes classificator">
                <b-form-radio-group id="bayesOptions" v-model="form.args.options['dist']" :options="distOptions">
                </b-form-radio-group>
              </b-form-group>
            </div>
            <div v-if="form.classification === 'svm'">
              <b-form-group label="Kernel" description="">
                <b-form-radio-group id="kernelOptions" v-model="form.args.options['kernel']" :options="kernelOptions">
                </b-form-radio-group>
              </b-form-group>
              <b-form-group label="C" description="">
                <b-form-radio-group id="cOptions" v-model="form.args.options['C']" :options="cOptions">
                </b-form-radio-group>
              </b-form-group>
              <b-form-group label="Gamma" description="Available only for rbf/poly/sigmoid kernel">
                <b-form-radio-group id="gammaOptions"
                                    v-model="form.args.options['gamma']"
                                    :options="gammaOptions"
                                    v-if="form.args.options['kernel'] === 'rbf' || form.args.options['kernel'] === 'poly' || form.args.options['kernel'] === 'signoid'"
                ></b-form-radio-group>
              </b-form-group>
            </div>
            <div v-if="form.classification === 'tree'">
              <b-form-group label="Criterion" description="">
                <b-form-radio-group id="criterionOptions" v-model="form.args.options['criterion']" :options="criterionOptions">
                </b-form-radio-group>
              </b-form-group>
              <b-form-group label="Splitter" description="">
                <b-form-radio-group id="splitterOptions" v-model="form.args.options['splitter']" :options="splitterOptions">
                </b-form-radio-group>
              </b-form-group>
              <b-form-group label="Minimal split of samples" description="Minimal value - 2">
                <b-form-input id="minSamplesSplitOptions" v-model="form.args.options['min_samples_split']" type="number">
                </b-form-input>
              </b-form-group>
            </div>
          <b-form-group label="Training data" label-for="file" description="Select training data">
            <b-form-file ref="fileinput" required v-model="form.file" :state="Boolean(form.file)" placeholder="Choose a file..."></b-form-file>
            <div class="mt-3">Selected file: {{form.file && form.file.name}}</div>
          </b-form-group>
          <b-form-checkbox id="checkbox" v-model="form.selection" value="true" onchecked-value="false">Use feature selection</b-form-checkbox>
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
        file: null,
        selection: ''
      },
      classificationOptions: [
        {text: 'Naive Bayes', value: 'bayes'},
        {text: 'Decision Tree', value: 'tree'},
        {text: 'SVM', value: 'svm'}
      ],
      argsOptions: {
        'bayes': {'dist': null},
        'svm': {'kernel': null, 'C': null, 'gamma': null},
        'tree': {'criterion': null, 'min_samples_split': 2, 'splitter': null}
      },
      distOptions: [
        {text: 'Gaussian Naive Bayes', value: 'GaussianNB'},
        {text: 'Multinominal Naive Bayes', value: 'MultinominalNB'}
      ],
      kernelOptions: [
        {text: 'Linear', value: 'linear'},
        {text: 'Poly', value: 'poly'},
        {text: 'RBF', value: 'rbf'},
        {text: 'Sigmoid', value: 'sigmoid'}
      ],
      cOptions: [
        {text: '10', value: 10.0},
        {text: '100', value: 100.0},
        {text: '1000', value: 1000.0}
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
    algChanged (checked) {
      this.form.args.options = {}
    },
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
      if (this.form.args.options['min_samples_split'] !== undefined) {
        this.form.args.options['min_samples_split'] = parseFloat(this.form.args.options['min_samples_split'])
      }
      let endpoint = this.form.classification + '/train'
      let formData = new FormData()
      formData.append('file', this.form.file)
      formData.append('options', JSON.stringify(this.form.args.options))
      formData.append('with_selection', this.form.selection)
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
