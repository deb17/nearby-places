<template>
  <b-alert v-model="show" variant="danger" dismissible class="mt-3">
      {{ message }}
  </b-alert>
</template>

<script>
  export default {
    props: ['message'],
    data () {
      return {
        show: true
      };
    }
  }
</script>
