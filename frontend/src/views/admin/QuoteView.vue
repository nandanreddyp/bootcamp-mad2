<script>

export default {
    name: 'QuoteView',
    data() {
        return {
            quote: null,
            quote_id: this.$route.params.id,
            message: '',
        };
    },
    mounted() {
        console.log('Quote ID:', this.$route.params.id);
        this.loadQuote(this.$route.params.id);
    },
    methods: {
        loadQuote(id) {
            const response = fetch(`http://127.0.0.1:5000/api/quotes/${id}`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`,
                    'Content-Type': 'application/json' // If you are sending JSON data
            },
            }).then( async response => {
                const data = await response.json();
                if (response.ok) {
                    return data;
                } else {
                    this.message = data.message || 'Loading quote failed';
                    throw new Error(data || 'Loading quote failed');
                }
            }).then((data) => {
                console.log(data);
                this.message = data.message;
                this.quote = data.quote;
            })
        },
        deleteQuotes(id) {
            const response = fetch(`http://127.0.0.1:5000/api/quotes/${id}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`,
                    'Content-Type': 'application/json' // If you are sending JSON data
            },
            }).then( async response => {
                const data = await response.json();
                if (response.ok) {
                    return data;
                } else {
                    this.message = data.message || 'Loading quotes failed';
                    throw new Error(data || 'Loading quotes failed');
                }
            }).then((data) => {
                console.log(data);
                this.message = data.message;
                alert(data.message);
                this.$router.push('/admin/quotes');
            })
        },

    }
};

</script>

<template>

    <h3>Quote</h3>

    <p v-if="!quote">Quote not found...</p>
    <p v-else>
            <h4>{{ quote.text }}</h4>
            <button v-on:click="deleteQuotes(quote.id)">Delete</button>
            <br>
            <a :href="`/admin/quotes/${quote.id}`">Edit Quote</a>
    </p>
    

    
</template>
