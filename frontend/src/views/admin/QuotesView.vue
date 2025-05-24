<template>
    <h2>Quotes page</h2>

        <h4>Create Quote</h4>
        <form id="quoteForm" @submit.prevent="createQuote" >
            <label for="text">Quote Text:</label>
            <textarea name="text" id="text" v-model="text" required></textarea>
            <input type="submit" value="Submit">
        </form>
        <p v-if="message">{{ message }}</p>

    <h3>Quotes</h3>

    <p v-if="!quotes">No Quotes yet...</p>
    <ul v-else>
        <li v-for="quote in quotes" :key="quote.id">
            <p>{{ quote.text }}</p>
            <button v-on:click="deleteQuotes(quote.id)">Delete</button>
            <br>
            <a :href="`/admin/quotes/${quote.id}`">Edit Quote</a>
        </li>
    </ul>
</template>

<script >

export default {
    name: 'QuotesView',
    data() {
        return {
            text: 'hi',
            message: '',
            quotes: [],
        };
    },
    methods: {

    createQuote() {
        const response = fetch('http://127.0.0.1:5000/api/quotes', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Content-Type': 'application/json' // If you are sending JSON data
        },
            body: JSON.stringify({
                text: this.text,
            }),
        }).then( async response => {
            const data = await response.json();
            if (response.ok) {
                return data;
            } else {
                this.message = data.message || 'Creating quote failed';
                throw new Error(data || 'Creating quote failed');
            }
        }).then((data) => {
            console.log(data);
            this.message = data.message;
            alert(data.message);
            this.loadQuotes();
        })
    },
    loadQuotes() {
        const response = fetch('http://127.0.0.1:5000/api/quotes', {
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
                this.message = data.message || 'Loading quotes failed';
                throw new Error(data || 'Loading quotes failed');
            }
        }).then((data) => {
            console.log(data);
            this.message = data.message;
            this.quotes = data.quotes;
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
            this.loadQuotes();
        })
    },


    },
    mounted() {
        this.loadQuotes();
    },
}

</script>