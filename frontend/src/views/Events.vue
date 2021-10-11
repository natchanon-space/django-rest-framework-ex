<template>
    <div class="calendar-events">
        <h1>List of events</h1>
        <div v-for="e in event_list" v-bind:key="e.id">
            <h2>{{ e.name }}</h2>
            <p>{{ e.description }}</p>
            <p>{{ e.start_date }}</p>
            <p>{{ e.end_date }}</p>
            <router-link v-bind:to="e.get_absolute_url">View detail</router-link>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Events',
    data() {
        return {
            event_list: []
        }
    },
    mounted() {
        this.getEventList()
    },
    methods: {
        getEventList() {
            const calendar_slug = this.$route.params.calendar_slug

            axios
                .get(`/api/v1/${calendar_slug}/events`)
                .then(response => {
                    this.event_list = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>