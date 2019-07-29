<template>
  <div class="col-12 col-sm-8 offset-sm-2 col-md-6 offset-md-3">
    <p class="lead mb-2">Search for places or entities nearest to you in your city.</p>
    <b-form @submit="onSubmit" class="text-center">
      <b-form-input
        id="input-1"
        v-model="form.query"
        size="lg"
        type="text"
        required
        placeholder="place in city"
      ></b-form-input>
      <div class="text-muted text-left mt-2"><i>Usage: Place in city. Eg. hotels in Delhi / restaurant in Bengaluru / coffee shop in New York</i></div>
      <p class="text-left mb-2"><a href="https://wiki.openstreetmap.org/wiki/Map_Features" target="_blank">What you can search for</a><small class="text-muted"> (Choose any key or value or both from &quot;Primary features&quot;.)</small></p>
      <b-button type="submit" variant="primary" size="lg">Submit</b-button>
      <br>
      <img src="../assets/ajax-loader.gif" v-show="show" class="mt-3">
    </b-form>
    <app-error-alert :message="errorMsg" v-if="showAlert"></app-error-alert>
    <b-modal id="modal-1" title="Enter an address" hide-footer>
      <b-form-textarea
        id="textarea"
        v-model="addr"
        placeholder="Address..."
        rows="4"
      ></b-form-textarea>
      <footer class="mt-2 float-right">
        <b-button variant="danger" @click="$bvModal.hide('modal-1')">Cancel</b-button>
        <b-button variant="primary" @click="sendAddr">OK</b-button>
      </footer>
    </b-modal>
  </div>
</template>

<script>
  import axios from 'axios';
  import ErrorAlert from './ErrorAlert.vue';
  export default {
    data() {
      return {
        form: {
          query: ''
        },
        show: false,
        results: [],
        user: {},
        errorMsg: '',
        showAlert: false,
        lat: null,
        lon: null,
        addr: ''
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault();
        this.showAlert = false;
        var resultData = {
          user: {},
          results: []
        };
        this.$emit('gotResults', resultData);

        if (this.lat == null && !this.addr) {
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(this.success, this.fail);
          } else {
            this.fail();
          }
        } else {
          this.getData();
        }
      },
      getData () {
        this.show = true;
        axios.get('https://debs-nearby-places.herokuapp.com/', {
          params: {
            s: this.form.query,
            lat: this.lat,
            lon: this.lon,
            addr: this.addr
          }
        }).then(response => {
          this.results = response.data;
          if (typeof this.results == "string") {
            this.errorMsg = this.results;
            this.showAlert = true;
            if (this.results.startsWith('Error: Address not found')) {
              this.addr = '';  
            }
            return;
          }
          this.user = this.results[0];
          this.user.name = "You";
          this.results.splice(0, 1);
          var resultData = {
            user: this.user,
            results: this.results
          };
          this.$emit('gotResults', resultData);
        }).catch(error => {
          this.errorMsg = 'Error fetching data from server. Try later.';
          this.showAlert = true;
        })
        .finally(() => { this.show = false; });
      },
      success(position) {
        this.lat = position.coords.latitude;
        this.lon = position.coords.longitude;
        this.getData();
      },
      fail(msg) {
        this.$bvModal.show('modal-1');
      },
      sendAddr() {
        if (this.addr) {
          this.$bvModal.hide('modal-1');
          this.getData();
        }
      }
    },
    components: {
      appErrorAlert: ErrorAlert
    }
  }
</script>

<style>
  
</style>
