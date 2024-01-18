<template>
    <div class="app-list-item">
      <img :src="app.image" alt="App Image" class="app-image" />
      <div class="app-details">
        <h3>{{ app.name }}</h3>
        <p>Points: {{ app.points }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      app: Object,
    }
  };
  </script>
  
  <style scoped>
  .app-list-item {
    display: flex;
    align-items: center;
    border: 1px solid #ddd;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  .app-image {
    max-width: 100px;
    margin-right: 20px;
  }
  
  .app-details {
    flex-grow: 1;
  }
  </style>
  