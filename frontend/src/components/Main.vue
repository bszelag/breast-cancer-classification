<template>
  <div>
    <b-jumbotron header="Breast Cancer Classification Tool" lead="Breast cancer classification by AI">
      <img src="../assets/logo.png">
      <p>Provide data from breast cytology and get results of our analysis!</p>
    </b-jumbotron>
    <!--<div d-flex justify-content-center>-->
      <!--<b-carousel id="carousel"-->
                  <!--style="text-shadow: 1px 1px 2px #333;"-->
                  <!--controls-->
                  <!--indicators-->
                  <!--background="#ababab"-->
                  <!--:interval="4000"-->
                  <!--img-height="80%"-->
                  <!--img-width="80%"-->
                  <!--v-model="slide"-->
                  <!--@sliding-start="onSlideStart"-->
                  <!--@sliding-end="onSlideEnd"-->
      <!--&gt;-->
        <!--<b-carousel-slide caption="Breast Cancer Classification"-->
                          <!--text="We can classify breast biopsy data using AI"-->
        <!--&gt;-->
          <!--<img slot="img" src="../assets/1.jpg">-->
        <!--</b-carousel-slide>-->
        <!--<b-carousel-slide caption="Our Goal"-->
                          <!--text="Out goal is to help you to understand data you have"-->
        <!--&gt;-->
          <!--<img slot="img" src="../assets/1.jpg">-->
        <!--</b-carousel-slide>-->
        <!--<b-carousel-slide caption="How it works?"-->
                          <!--text="You need to choose classification algorithm and provide data. We're dealing with rest!"-->
        <!--&gt;-->
          <!--<img slot="img" src="../assets/3.jpg">-->
        <!--</b-carousel-slide>-->
      <!--</b-carousel>-->
    <!--</div>-->
  </div>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
