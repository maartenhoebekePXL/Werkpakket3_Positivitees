<template>
  <main>
    <LayoutComponent>
      <div v-if="currentFase === 0" class="welcomeSection">
        <h1>WanderTrails</h1>
        <p>
          Ontdek de wereld met WanderTrails. Verken adembenemende routes, deel avonturen en vind je
          volgende outdoor-ervaring in een handomdraai. Welkom bij jouw ultieme gids voor wandelen,
          kanoën en meer.
        </p>
        <button @click="startOnboarding">Laat je avontuur beginnen!</button>
      </div>
      <div v-if="currentFase === 1" class="questionsSection">
        <div class="questionsSection-progress">
          <div
            v-for="(question, index) in questions"
            :key="index"
            class="questionsSection-progress-oval"
            :class="{ active: currentQuestionIndex === index }"
          ></div>
          <div>
            <p>Stap {{ currentQuestionIndex + 1 }} van {{ questions.length }}</p>
          </div>
        </div>
        <transition name="fade">
          <div class="questionsSection-question" v-if="showQuestion">
            <!-- Display only the current question -->
            <p>{{ currentQuestion.question }}</p>
            <div class="questionsSection-question-options">
              <div
                v-for="(option, optionIndex) in currentQuestion.options"
                :key="optionIndex"
                class="questionsSection-question-options-option"
                @click="selectOption(currentQuestionIndex, option)"
                :class="{ selected: isSelected(option) }"
              >
                <span>{{ option }}</span>
              </div>
            </div>
          </div>
        </transition>
        <div class="questionsSection-buttons">
          <button class="previous" @click="previousQuestion" :disabled="currentQuestionIndex === 0">
            Vorige
          </button>
          <button class="next" @click="nextQuestion">Volgende</button>
          <button class="skip" @click="skipQuestions">Skip, ik vul dit later in</button>
        </div>
      </div>
    </LayoutComponent>
  </main>
</template>

<script>
import LayoutComponent from '@/components/LayoutComponent.vue'

export default {
  components: {
    LayoutComponent
  },
  data() {
    return {
      questions: [
        {
          question: 'What is jouw leeftijd?',
          options: ['16 - 24 jaar oud', '25 - 55 jaar oud', '55+ jaar oud']
        },
        {
          question: 'Hoeveel keer per week ga je sporten?',
          options: ['0 - 1 keer', '1 - 3 keer', '4+ keer']
        },
        {
          question: 'In welke omgeving sport je het liefst?',
          options: ['Bos & Natuur', 'Stad', 'Platteland']
        },
        {
          question: 'Hoe lang ga je gemiddeld sporten?',
          options: ['0 - 1 uur', '1 - 3 uur', '4+ uur']
        }
      ],
      selectedOptions: [],
      currentQuestionIndex: 0,
      currentFase: 0,
      showQuestion: true
    }
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex]
    }
  },
  methods: {
    startOnboarding() {
      this.currentFase++
    },
    nextQuestion() {
      if (this.currentQuestionIndex < this.questions.length - 1) {
        this.showQuestion = false
        setTimeout(() => {
          this.currentQuestionIndex++
          this.showQuestion = true
        }, 300)
      } else {
        console.log('Navigating to EmptyStateView')
        this.$router.push({ name: 'EmptyStateView' })
      }
    },
    previousQuestion() {
      if (this.currentQuestionIndex > 0) {
        this.showQuestion = false
        setTimeout(() => {
          this.currentQuestionIndex--
          this.showQuestion = true // Show question after short delay
        }, 300) // Adjust the delay as needed
      }
    },
    skipQuestions() {
      this.selectedOptions.splice(this.currentQuestionIndex, 1)
      this.nextQuestion()
    },
    selectOption(questionIndex, option) {
      this.selectedOptions[questionIndex] = option
    },
    isSelected(option) {
      return this.selectedOptions[this.currentQuestionIndex] === option
    },
    areAllQuestionsCompleted() {
      // Logic to check if all questions are completed
      return true // For demonstration purposes, assuming all questions are completed
    }
    // Method to navigate to EmptyStateView when all questions are completed
    // navigateToEmptyState() {
    //   if (this.areAllQuestionsCompleted()) {
    //     this.$router.push({ name: 'EmptyState' })
    //   }
    // }
  },
  watch: {
    currentQuestionIndex: {
      handler() {
        // Call navigateToEmptyState whenever currentQuestionIndex changes
        // this.navigateToEmptyState()
      },
      immediate: true // Call handler immediately when component is mounted
    }
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
