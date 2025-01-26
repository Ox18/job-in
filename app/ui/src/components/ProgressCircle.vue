<script>
export default {
  props: {
    isPlaying: Boolean,
    progress: Number,
  },
  computed: {
    progressStyle() {
      const degrees = (this.progress / 100) * 360;
      return {
        background: `conic-gradient(black ${degrees}deg, gray ${degrees}deg)`,
      };
    },
  },
  methods: {
    onToggle() {
      this.$emit("toggle");
    },
  },
};
</script>
<template>
  <div
    class="flex justify-center items-center relative cursor-pointer hover:opacity-80 transition-opacity active:opacity-100"
    @click="onToggle"
  >
    <div class="fixed w-25 h-25">
      <div
        class="absolute w-full h-full rounded-full bg-black"
        :style="progressStyle"
      ></div>
    </div>
    <div class="relative w-23 h-23">
      <div
        class="absolute w-full h-full rounded-full bg-black border-4 border-white"
      >
        <div
          class="flex justify-center items-center w-full h-full rounded-full"
        >
          <span class="text-l font-bold text-white">
            <svg
              v-if="isPlaying"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-10"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15.75 5.25v13.5m-7.5-13.5v13.5"
              />
            </svg>
            <svg
              v-else
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-10"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5.25 5.653c0-.856.917-1.398 1.667-.986l11.54 6.347a1.125 1.125 0 0 1 0 1.972l-11.54 6.347a1.125 1.125 0 0 1-1.667-.986V5.653Z"
              />
            </svg>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
