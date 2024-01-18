<template>
    <div>
      <div class="app-details">
        <h3>{{ app.name }}</h3>
        <p>Points: {{ app.points }}</p>
      </div>
      <div
        id="drop-area"
        @dragover.prevent="handleDragOver"
        @dragleave.prevent="handleDragLeave"
        @drop.prevent="handleDrop"
        :class="{ highlight: isHighlight }"
      >
        <p>Drag and drop an image here, or click to select one</p>
        <input type="file" id="file-input" @change="handleFileSelect" />
      </div>
  
      <img id="preview" :src="previewImage" alt="Preview Image" v-if="previewImage" />
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isHighlight: false,
        previewImage: null,
        apps: [
        { id: 1, name: 'App 1', points: 100, image: 'path-to-image-1.jpg' },
        { id: 2, name: 'App 2', points: 150, image: 'path-to-image-2.jpg' },
        // Add more app data as needed
      ],
      };
    },
    methods: {
      handleDragOver() {
        this.isHighlight = true;
      },
      handleDragLeave() {
        this.isHighlight = false;
      },
      handleDrop(event) {
        this.isHighlight = false;
        const files = event.dataTransfer.files;
  
        if (files.length > 0) {
          this.handleFile(files[0]);
        }
      },
      handleFileSelect(event) {
        const files = event.target.files;
  
        if (files.length > 0) {
          this.handleFile(files[0]);
        }
      },
      handleFile(file) {
        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
  
          reader.onload = () => {
            this.previewImage = reader.result;
          };
  
          reader.readAsDataURL(file);
        } else {
          alert('Please select an image file.');
        }
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
  
  #file-input {
    display: none;
  }
  
  img {
    max-width: 100%;
    max-height: 200px;
    margin-top: 20px;
  }
  </style>
  