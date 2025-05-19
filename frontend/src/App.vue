<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'


function logout() {
  if (confirm('Are you sure you want to logout?')) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      this.$router.push('/in');
      return;
  } else{
    return;
  }
};

const user = JSON.parse(localStorage.getItem('user'));

</script>

<template>
  <header style="display: flex; align-items: center; padding: 20px;">
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" />
    
    <nav style="display: flex; gap: 20px">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <a href="#" v-if="user" @click="logout">Logout</a>
    </nav>

  </header>

  <RouterView />

</template>

<style scoped>
</style>
