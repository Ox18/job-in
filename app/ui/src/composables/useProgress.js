import { ref } from "vue";

export const useProgress = (time) => {
  const duration = ref(time);
  const isPlaying = ref(true);
  const progress = ref(0);
  const intervalId = ref(null);

  const start = () => {
    const increment = 100 / duration.value;
    intervalId.value = setInterval(() => {
      if (progress.value < 100) {
        progress.value += increment;
      } else {
        clearInterval(intervalId.value);
        isPlaying.value = false;
      }
    }, 1000);
  };

  const reset = () => {
    progress.value = 0;
  };

  const stop = () => {
    clearInterval(intervalId.value);
    isPlaying.value = false;
  };

  const toggle = () => {
    isPlaying.value = !isPlaying.value;
    if (isPlaying.value) {
      start();
    } else {
      stop();
    }
  };

  return {
    duration,
    isPlaying,
    progress,
    start,
    reset,
    stop,
    toggle,
  };
};
