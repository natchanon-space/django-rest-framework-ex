<template>
  <div class="home">
    <div v-for="c in calendar_list" v-bind:key="c.id">
      <div class="box">
        <h2>{{ c.name }}</h2>
        <router-link v-bind:to="c.get_absolute_url">View events list</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      calendar_list: []
    }
  },
  components: {

  },
  mounted() {
    this.getCalendarList()
  },
  methods: {
    getCalendarList() {
      axios
        .get('/api/v1/calendar-list/')
        .then(response => {
          this.calendar_list = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
