<script>
import { useMainView } from "@/composables/useMainView";
import Loading from "@/components/Loading.vue";
import Buble from "@/components/Buble.vue";

const { jobs, load, isLoading } = useMainView();

export default {
  name: "MainView",
  components: {
    Loading,
    Buble,
  },
  setup() {
    return { jobs, load, isLoading };
  },
  created() {
    load();
  },
  methods: {
    submit() {
      this.$router.push("/find");
    },
  },
};
</script>
<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <Loading />
  </div>
  <div v-else class="flex justify-center items-center h-screen flex-col gap-18">
    <div class="flex flex-wrap justify-center gap-4 max-w-3xl">
      <template v-for="job in jobs" :key="job.id">
        <Buble :src="job.logo_url" />
      </template>
    </div>
    <div class="text-center max-w-3xl">
      <h1 class="text-5xl font-bold tracking-wider text-black">
        <!-- Find your <span class="text-blue-500">dream job</span>
        and work with us -->
        Encuentra tu <span class="text-pink-500">próximo gran paso</span>
        profesional
      </h1>
      <p class="mt-4 text-lg text-gray-300">
        Explora oportunidades únicas y postula a trabajos que se ajusten a tus
        habilidades y aspiraciones. Con un solo clic, puedes avanzar en tu
        carrera.
      </p>
    </div>

    <div>
      <button
        @click="submit"
        type="button"
        class="px-6 py-3.5 text-base font-medium text-white bg-gray-800 hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700 dark:border-gray-700"
      >
        Iniciar búsqueda
      </button>
    </div>
  </div>
</template>
