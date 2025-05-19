<template>
  <div class="about">
    <h1>This is an auth page</h1>

    <div v-if="isLogin">
        <h2>Login</h2>
        <p>Enter your credentials to log in.</p>
        <form id="loginForm" @submit.prevent="loginUser" >
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" v-model="email" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="password" required>
            <input type="submit" value="Submit">
        </form>
        <p v-if="message">{{ message }}</p>
        <p>Don't have an account? <button @click="toggleForm()" >Register here</button></p>
    </div>

    <div v-else>
        <h2>Registration</h2>
        <p>Enter your credentials to log in.</p>
        <form id="loginForm" @submit.prevent="registerUser" >
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" v-model="name" required>            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" v-model="email" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="password" required>
            <input type="submit" value="Submit">
        </form>
        <p v-if="message">{{ message }}</p>
        <p>Have an account? <button @click="toggleForm()" >Login here</button></p>
    </div>



  </div>
</template>

<script>

export default {
  name: 'AuthView',
  data() {
    return {
        isLogin: true,
        message: '',
        name: '',
        email: '',
        password: '',
      // Define any data properties you need here
    };
  },
  methods: {
    toggleForm() {
        this.message = '';        
        this.isLogin = !this.isLogin;
    },
    loginUser() {
        const response = fetch('http://127.0.0.1:5000/api/auth', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: this.email,
                password: this.password,
            }),
        }).then( async response => {
            const data = await response.json();
            if (response.ok) {
                return data;
            } else {
                this.message = data.message || 'Login failed';
                throw new Error(data || 'Login failed');
            }
        }).then((data) => {
            console.log(data);
            this.message = data.message;
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('user', JSON.stringify(data.user));
            this.$router.push('/');
            window.location.reload();
        })
    },
    registerUser() {
        const response = fetch('http://127.0.0.1:5000/api/auth', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: this.name,
                email: this.email,
                password: this.password,
            }),
        }).then( async response => {
            const data = await response.json();
            if (response.ok) {
                return data;
            } else {
                this.message = data.message || 'Login failed';
                throw new Error(data || 'Login failed');
            }
        }).then((data) => {
            console.log(data);
            this.message = data.message;
        })
    }
  },
  mounted() {
    
  },
};


</script>
