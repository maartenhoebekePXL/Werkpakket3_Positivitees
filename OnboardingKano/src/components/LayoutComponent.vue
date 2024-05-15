<template>
  <div class="layout">
    <div class="layout-left">
      <img src="@/assets/Forrest.png" alt="Forest Image" class="background-image" />
      <NavigationComponent></NavigationComponent>
      <div class="content-box">
        <slot></slot>
      </div>
    </div>
    <div class="layout-right">
      <img src="@/assets/Ocean.png" alt="Ocean Image" class="background-image" />
      <div class="gradient"></div>
      <div class="layout-right-image">
        <img :src="contentImages[currentImageIndex]" alt="Dynamic Image" />
      </div>
    </div>
  </div>
</template>

<script>
import NavigationComponent from './NavigationComponent.vue'

export default {
  components: {
    NavigationComponent
  },
  data() {
    return {
      contentImages: [
        'src/assets/Image1.png',
        'src/assets/Image2.png',
        'src/assets/Image3.png',
        'src/assets/Image4.png',
        'src/assets/Image5.png',
        'src/assets/Image6.png',
        'src/assets/Image7.png'
      ],
      currentImageIndex: 0
    }
  },
  watch: {
    '$parent.currentFase': 'updateCurrentImageIndex',
    '$parent.currentQuestionIndex': 'updateCurrentImageIndex'
  },
  computed: {
    currentImageSrc() {
      return this.contentImages[this.currentImageIndex]
    }
  },
  methods: {
    updateCurrentImageIndex() {
      if (this.$parent.currentFase === 0) {
        this.currentImageIndex = 0
      } else {
        this.currentImageIndex = this.$parent.currentQuestionIndex + 1
      }
    }
  }
}
</script>
