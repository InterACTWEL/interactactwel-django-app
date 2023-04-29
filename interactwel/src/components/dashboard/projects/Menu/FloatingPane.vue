<template>
    <div class="floating-pane">
      <div class="header">
        <button @click="toggle">Open/Close</button>
      </div>
      <div class="content">
        <!-- Add your content here -->
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    }
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen
    }
  }
}
</script>


<style scoped>
.floating-pane {
  position: absolute;
  top: 50px;
  left: 50px;
  width: 300px;
  height: 200px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

.header {
  background-color: #f0f0f0;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.content {
  padding: 10px;
}
</style>

  