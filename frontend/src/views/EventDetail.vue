<template>
    <div class="calendar-detail">
        <h2>{{ calendar_event.name }}</h2>
        <p>{{ calendar_event.description }}</p>
        <p>Start Date: {{ calendar_event.start_date }}</p>
        <p>End Date: {{ calendar_event.end_date }}</p>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'EventDetail',
    data() {
        return {
            calendar_event: {}
        }
    },
    mounted() {
        this.getEvent()
    },
    methods: {
        getEvent() {
            const calendar_slug = this.$route.params.calendar_slug
            const event_slug = this.$route.params.event_slug

            axios
                .get(`/api/v1/${calendar_slug}/${event_slug}`)
                .then(response => {
                    this.calendar_event = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>