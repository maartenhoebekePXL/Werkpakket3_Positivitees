<template>
  <main>
    <LayoutComponent>
      <div class="rows">
        <div class="row1">
          <div class="health" id="cals">
            <div class="health-title">
              <img src="@/assets/Fire.png" alt="Fire" />
              <p>Calorieën</p>
            </div>
            <div class="health-counter">
              <p><span>0</span>kcal</p>
            </div>
          </div>
          <div class="health" id="heartBeat">
            <div class="health-title">
              <img src="@/assets/Heart with Pulse.png" alt="Heart" />
              <p>Hartslag</p>
            </div>
            <div class="health-counter">
              <p><span>0</span>bpm</p>
            </div>
          </div>
          <div class="health" id="steps">
            <div class="health-title">
              <img src="@/assets/Footprint.png" alt="Feet" />
              <p>Stappen</p>
            </div>
            <div class="health-counter">
              <p><span>0</span>stappen</p>
            </div>
          </div>
        </div>
        <div class="row2">
          <p class="row2-title">Voorgestelde Routes</p>
          <div class="row2-boxes">
            <div class="row2-boxes-row1">
              <div @click="changeSrc" class="BigActivity">
                <div class="BigActivity-div">
                  <p>Boswandeling</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <p><span>15</span>km</p>
                <img class="activityImg" src="@/assets/Boswandeling.png" alt="#" />
              </div>
              <div @click="changeSrc" class="BigActivity">
                <div class="BigActivity-div">
                  <p>Natuurwandeling</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <p><span>7</span>km</p>
                <img class="activityImg" src="@/assets/LangsNatuur.png" alt="#" />
              </div>
            </div>
            <div class="row2-boxes-row2">
              <div class="SmallActivity">
                <p>In het veld</p>
                <div class="SmallActivity-div">
                  <p><span>10</span>km</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <img class="activityImg" src="@/assets/Veld.png" alt="#" />
              </div>
              <div class="SmallActivity">
                <p>Langs rivier</p>
                <div class="SmallActivity-div">
                  <p><span>4</span>km</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <img class="activityImg" src="@/assets/Rivier.png" alt="#" />
              </div>
              <div class="SmallActivity">
                <p>Op 't meer'</p>
                <div class="SmallActivity-div">
                  <p><span>9</span>km</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <img class="activityImg" src="@/assets/Meer.png" alt="#" />
              </div>
              <div class="SmallActivity">
                <p>Looptocht</p>
                <div class="SmallActivity-div">
                  <p><span>20</span>km</p>
                  <img src="@/assets/Favorite.png" alt="heart" />
                </div>
                <img class="activityImg" src="@/assets/Looptocht.png" alt="#" />
              </div>
            </div>
          </div>
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
    return {}
  },
  method: {
    changeSrc() {
      this.heartImageSrc = '@/assets/HeartFilled.png'
    }
  }
}
</script>
