<template>
  <div>
    <h2>App List</h2>
    <AppListItem v-for="app in apps" :key="app.id" :app="app" />
  </div>
</template>

<script>
import AppListItem from './AppListItem.vue';

export default {
  data() {
    return {
      apps: [
        { id: 1, name: 'App 1', points: 100, image:'C:\Users\sudhi\OneDrive\Desktop\project\facebook.png' },
        { id: 2, name: 'App 2', points: 150, image: '\linkedin.png' },
        { id: 3, name: 'App 3', points: 250, image: '\snapchat.png' },
        // Add more app data as needed
      ],
    };
  },
  components: {
    AppListItem,
  },
};
</script>
