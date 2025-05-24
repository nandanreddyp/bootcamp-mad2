<script setup>
import { RouterLink, RouterView } from 'vue-router'


var user = JSON.parse(localStorage.getItem('user'))

function logout() {
  if (confirm('Are you sure you want to logout?')) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      this.user = null;
      this.$router.push('/in');
      window.location.reload();
  } else{
    return;
  }
};


</script>

<template>
  <header style="display: flex; align-items: center; padding: 20px;">
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" />
    <h1>This is my Vue Application</h1>
    
    <nav style="display: flex; gap: 20px">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <a href="#" v-if="user" @click="logout">Logout</a>
    </nav>

  </header>

  <RouterView  />

</template>

<style>

/* Reset some default styles */
body, h1, h2, p, form, input, label, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    /* display: flex; */
    /* align-items: flex-start; */
    /* min-height: 100vh; */
}

/* Container styling */
div {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 100%;
    /* max-width: 400px; */
}

/* Headings */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

h2 {
    margin-bottom: 10px;
    color: #333;
}

/* Paragraphs */
p {
    margin-bottom: 15px;
    color: #555;
}

/* Form inputs */
form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #333;
}

input[type="email"],
input[type="password"],
input[type="text"] {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

/* Submit button */
input[type="submit"] {
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 15px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #0056b3;
}

/* Toggle form button */
button {
    background: none;
    border: none;
    color: #007BFF;
    text-decoration: underline;
    cursor: pointer;
    font-size: 14px;
    padding: 0;
}

button:hover {
    color: #0056b3;
}


</style>
