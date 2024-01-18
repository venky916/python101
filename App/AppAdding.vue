<template>
  <div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="appName">App Name:</label>
        <input type="text" id="appName" v-model="appName" required />
      </div>

      <div>
        <label for="appPoints">App Points:</label>
        <input type="number" id="appPoints" v-model="appPoints" required />
      </div>

      <div>
        <label for="appImage">App Image:</label>
        <div id="drop-area" @dragover.prevent="handleDragOver" @dragleave.prevent="handleDragLeave" @drop.prevent="handleDrop" :class="{ highlight: isImageHighlight }">
          <p>Drag and drop an image here, or click to select one</p>
          <input type="file" id="appImageInput" @change="handleFileSelect" />
        </div>
        <img id="appImagePreview" :src="appImagePreview" alt="App Image" v-if="appImagePreview" />
      </div>

      <div>
        <label for="appCategory">App Category:</label>
        <select id="appCategory" v-model="appCategory" required>
          <option value="social">Social</option>
          <option value="utility">Utility</option>
          <!-- Add more categories as needed -->
        </select>
      </div>

      <div>
        <label for="subCategory">Sub Category:</label>
        <select id="subCategory" v-model="subCategory" required>
          <!-- Add subcategories based on the selected category -->
        </select>
      </div>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      appName: '',
      appPoints: 0,
      appImage: null,
      appImagePreview: null,
      appCategory: 'social',
      subCategory: '',
      isImageHighlight: false,
    };
  },
  methods: {
    handleDragOver(event) {
      this.isImageHighlight = true;
    },
    handleDragLeave(event) {
      this.isImageHighlight = false;
    },
    handleDrop(event) {
      this.isImageHighlight = false;
      const files = event.dataTransfer.files;

      if (files.length > 0) {
        this.handleFileSelect(files[0]);
      }
    },
    handleFileSelect(file) {
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = () => {
          this.appImage = file;
          this.appImagePreview = reader.result;
        };

        reader.readAsDataURL(file);
      } else {
        alert('Please select an image file.');
      }
    },
    submitForm() {
      // Implement your form submission logic here
      console.log('Form submitted!', this.appName, this.appPoints, this.appImage, this.appCategory, this.subCategory);
    },
  },
  watch: {
    appCategory(newCategory) {
      // Update subcategories based on the selected category
      // You can fetch subcategories from an API or define them manually
      // For simplicity, we'll use a static list
      if (newCategory === 'social') {
        this.subCategories = ['Messaging', 'Social Networking', 'News'];
      } else if (newCategory === 'utility') {
        this.subCategories = ['Productivity', 'Tools', 'Health'];
      }
      // Add more cases based on your categories
      // Update the options of the subcategory dropdown dynamically
      this.subCategory = this.subCategories[0]; // Set default subcategory
    },
  },
};
</script>

<style scoped>
#drop-area {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
  cursor: pointer;
}

#drop-area.highlight {
  border-color: #2196F3;
  color: #2196F3;
}

#appImagePreview {
  max-width: 100%;
  max-height: 200px;
  margin-top: 20px;
}
</style>
