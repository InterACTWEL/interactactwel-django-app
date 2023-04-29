<template>
  <div class="container-fluid">
    <b-row>
      <b-col>
        <h6 class="mt-3">
          <div class="title">
            <b-nav pills>
              <b-nav-item>Adaptation Plan {{ $route.params.planId }}</b-nav-item>
            </b-nav>
            <div>
              <!-- Sidebar toggle button -->
              <b-button variant="success" @click="showSidebar = true">
                Feedback
              </b-button>
            </div>
          </div>
        </h6>
        <router-view :key="$route.fullPath" />
      </b-col>
    </b-row>
    <div class="sidebar-container">
      <b-container fluid>
        <b-sidebar v-model="showSidebar" 
        position="start" 
        title="Feedback">
          <FeedbackPage />
        </b-sidebar>
      </b-container>
    </div>
  </div>
</template>

<script>
import FeedbackPage from '@/components/dashboard/projects/charts/Feedback.vue';

export default {
  name: "Visualization",
  components: {
    FeedbackPage,
  },
  data() {
    return {
      showSidebar: false,
    };
  },
};
</script>

<style scoped>
.container-fluid {
  padding: 0;
}

.title {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.sidebar-container {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  z-index: 1000;
}

.sidebar-wrapper {
  display: flex;
  flex-direction: row;
  height: 100%;
}

.sidebar-content {
  width: 100%;
  padding: 15px;
  flex: 1;
}
</style>
