<template>
   <div>
    <Header :username="username" />
    <div class="flex-container">
      <Sidebar />
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Sidebar from '@/components/SideBar.vue';

export default {
  components: {
    Header,
    Sidebar,
  },
  data() {
    return {
      username: 'YourUsername', // Replace with the actual username
    };
  },
  // You can perform authenticated actions here
  // Use the token stored in localStorage for authentication
  created() {
    const token = localStorage.getItem('token');
    if (!token) {
      this.$router.push('/login');
    }
    // Use the token for authenticated API requests
    // (Note: You should replace the API_URL with your actual API endpoint)
    axios.get('API_URL/some-authenticated-endpoint/', {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then(response => {
        // Handle the response
      })
      .catch(error => {
        console.error('Authenticated request failed:', error);
      });
  },
};
</script>

