<template>
  <div>
      <h2>App List</h2>
      <div v-for="app in apps" :key="app.id" @click="showAppDetails(app)">
        <div class="app-item">
          <img :src="app.image" alt="App Image" />
          <p>{{ app.name }}</p>
          <p>Points: {{ app.points }}</p>
        </div>
        </div>
      </div>

  </template>
  
  <script>
  export default {
    data() {
      return {
        apps: [ /* your app data goes here */ ],
      };
    },
    methods: {
      showAppDetails(app) {
        this.$router.push({ name: 'app-details', params: { id: app.id } });
      },
    },
  };
  </script>
  
  <style scoped>
  .app-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    display: inline-block;
    cursor: pointer;
  }
  </style>