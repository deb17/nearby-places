<template>
  <GmapMap
    :center="{lat: output.user.lat, lng: output.user.lon}"
    :zoom="14"
    map-type-id="terrain"
    style="width: 80vw; height: 80vh; margin: 0px auto 20px;"
  >
    <GmapMarker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :title="m.title"
      :label="m.label"
      :icon="m.icon"
    />
  </GmapMap>    
</template>

<script>
  export default {
    props: ['output'],
    computed: {
      markers () {
        var arr = [];
        this.output.results.forEach((res, index) => {
          arr.push({ 
                     position: { lat: res.lat, lng: res.lon },
                     title: res.name,
                     label: (index+1).toString(),
                     icon: ''
          });
        });
        arr.push({ 
                    position: { lat: this.output.user.lat, lng: this.output.user.lon },
                    title: 'You',
                    label: 'You',
                    icon: 'http://maps.google.com/mapfiles/ms/icons/ylw-pushpin.png'
        });
        return arr;
      }
    }
  }
</script>

<style>
  
</style>
