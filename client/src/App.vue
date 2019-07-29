<template>
  <div class="container mt-2">
    <h1 class="text-center mb-4 display-4">Search nearby places</h1>
    <div class="row">
      <app-srchform @gotResults="output = $event"></app-srchform>
    </div>
    <div v-if="output.results.length > 0">
      <app-result :items="output.results"></app-result>
      <div id="zoomout" class="mb-2"><small>You may need to zoom out the map to see all the markers.</small></div>
      <app-mapinfo :output="output"></app-mapinfo>
    </div>
  </div>
</template>

<script>
  import Srchform from './components/Srchform.vue';
  import Result from './components/Result.vue';
  import Mapinfo from './components/Mapinfo.vue';

  export default {
    data () {
      return {
        output: {
          user: {},
          results: []
        }
      };
    },
    components: {
      appSrchform: Srchform,
      appResult: Result,
      appMapinfo: Mapinfo
    }
  }
</script>

<style>
  body {
    background-color: #e6f5ff;
    color: #333;
    font-family: Arial, Helvetica, sans-serif;
  }
  h1 {
    font-family: 'Damion', cursive;
    color: #666;
  }
  #zoomout {
    width: 80vw;
    margin: 0 auto;
    line-height: 1.1;
  }
</style>
