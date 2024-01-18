<template>
    <div>
      <h2>App Details</h2>
      <div>
        <img :src="app.image" alt="App Image" />
        <p>{{ app.name }}</p>
        <p>Points: {{ app.points }}</p>
      </div>
      <div>
        <h3>Upload Screenshot</h3>
        <input type="file" @change="handleFileUpload" />
        <!-- Add additional UI for drag and drop -->
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        app: null,
      };
    },
    created() {
      // Fetch the app details based on the route params (app id)
      // You can use a Vuex store or make an API request here
      const appId = this.$route.params.id;
      // Fetch the app details based on appId and set it to 'app' data property
      // Example: this.app = fetchAppDetails(appId);
    },
    methods: {
      handleFileUpload(event) {
        const file = event.target.files[0];
        // Handle file upload logic here
      },
    },
  };
</script>