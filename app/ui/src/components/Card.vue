<script>
import { timeAgo } from "@/shared/utils/time";
import ProgressCircle from "@/components/ProgressCircle.vue";
import CardSkeleton from "./CardSkeleton.vue";
import ButtonReject from "@/components/ButtonReject.vue";
import ButtonSeeLater from "@/components/ButtonSeeLater.vue";
import ButtonAccept from "./ButtonAccept.vue";
import ButtonOpen from "./ButtonOpen.vue";
import { useProgress } from "@/composables/useProgress";

export default {
  name: "CardComponent",
  components: {
    ProgressCircle,
    CardSkeleton,
    ButtonReject,
    ButtonSeeLater,
    ButtonAccept,
    ButtonOpen,
  },
  setup() {
    const { isPlaying, progress, start, reset, stop, toggle } = useProgress(25);
    return {
      isPlaying,
      progress,
      start,
      reset,
      stop,
      toggle,
    };
  },
  props: {
    job: {
      type: Object,
      required: true,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    timeAdapted() {
      if (!this.job.time_response) return "No especificado";
      const result = this.job.time_response.match(/\d+/);
      return `${result} días`;
    },
    timeSincePosted() {
      return timeAgo(this.job.listed_date);
    },
  },
  methods: {
    onCardExpired() {
      this.$emit("expired");
    },
    onAccept() {
      this.$emit("accept");
    },
    onReject() {
      this.$emit("reject");
    },
    onSeeLater() {
      this.$emit("see-later");
    },
    onOpen() {
      this.$emit("open");
      this.stop();
    },
  },
  mounted() {
    this.start();
  },
  watch: {
    progress(newVal) {
      if (newVal >= 100) {
        this.onCardExpired();
      }
    },
  },
};
</script>
<template>
  <CardSkeleton v-if="loading" />
  <div
    v-else
    class="p-8 bg-white border border-gray-200 rounded-lg shadow-lg dark:bg-gray-800 dark:border-gray-700 w-96 flex flex-col justify-center items-center gap-6 transition-transform transform hover:scale-105 pb-20 h-full relative pb-30"
    style="height: 500px"
  >
    <img
      class="rounded-full w-27 h-27 border-2 border-gray-200"
      :src="job.logo_url"
      alt="image description"
    />

    <div class="flex flex-col justify-center items-center gap-3">
      <p class="text-lg font-semibold text-gray-400 dark:text-gray-100">
        {{ job.company_name }}
      </p>
      <h1 class="text-3xl font-bold text-gray-900 dark:text-white text-center">
        {{ job.title }}
      </h1>
      <p
        class="bg-blue-100 text-blue-800 text-sm font-medium px-3 py-1 rounded-full dark:bg-blue-900 dark:text-blue-300"
      >
        {{ job.modality }}
      </p>
    </div>
    <div
      class="w-full flex flex-col gap-2 text-sm text-gray-600 dark:text-gray-400"
    >
      <div class="flex justify-between">
        <span>Country:</span>
        <span class="font-medium">{{ job.country }}</span>
      </div>
      <div class="flex justify-between">
        <span>Ubigeo:</span>
        <span class="font-medium">{{ job.ubigeo }}</span>
      </div>
      <div class="flex justify-between">
        <span>Reposted:</span>
        <span class="font-medium">{{ job.reposted ? "Si" : "No" }}</span>
      </div>
      <div class="flex justify-between">
        <span>Application Type:</span>
        <span class="font-medium">{{ job.application_type }}</span>
      </div>
      <div class="flex justify-between">
        <span>Publicación:</span>
        <span class="font-medium">{{ timeSincePosted }}</span>
      </div>
      <div class="flex justify-between">
        <span>Tiempo de respuesta:</span>
        <span class="font-medium">{{ timeAdapted }}</span>
      </div>
    </div>
    <div class="container__timer">
      <ProgressCircle
        :progress="progress"
        :isPlaying="isPlaying"
        @toggle="toggle"
      />
    </div>
  </div>
  <div v-if="!loading" class="flex justify-center gap-4 mt-10">
    <ButtonOpen @click="onOpen" />
    <ButtonAccept @click="onAccept" />
    <ButtonReject @click="onReject" />
    <ButtonSeeLater @click="onSeeLater" />
  </div>
</template>
<style scoped>
.container__timer {
  position: absolute;
  bottom: -48px;
}
</style>
