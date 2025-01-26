<script>
export default {
  name: "FeedbackComponent",
  props: {
    modelValue: {
      type: Object,
      required: true,
    },
  },
  watch: {
    modelValue: {
      handler(newValue) {
        console.log(newValue);
      },
      deep: true,
    },
  },
  computed: {
    title() {
      return this.modelValue.headerContent;
    },
    itemsMatch() {
      return this.modelValue.matchSection.items;
    },
    titleItemsMatch() {
      return this.modelValue.matchSection.title;
    },
  },
};
</script>
<template>
  <div class="bg-white rounded-lg shadow-md p-6 max-w-md mx-auto">
    <!-- Título principal -->
    <h1 class="text-xl font-bold text-gray-800 mb-4">{{ title }}</h1>

    <!-- Sección de coincidencias -->
    <div>
      <!-- Título de la sección de coincidencias -->
      <h2 class="text-lg font-semibold text-gray-700 mb-4">
        {{ titleItemsMatch }}
      </h2>

      <!-- Lista de elementos coincidentes -->
      <div v-for="item in itemsMatch" :key="item.title" class="mb-6">
        <!-- Título del elemento -->
        <p class="text-md font-medium text-gray-900 mb-2">{{ item.title }}</p>

        <!-- Estado del elemento -->
        <div class="flex items-center mb-2">
          <svg
            v-if="item.status === 'SIGNAL_POSITIVE'"
            class="w-4 h-4 mr-2 text-green-600"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"
            />
          </svg>
          <svg
            v-else-if="item.status === 'SIGNAL_NEUTRAL'"
            class="w-4 h-4 mr-2 text-yellow-600"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 000 2h6a1 1 0 100-2H7z"
              clip-rule="evenodd"
            />
          </svg>
          <p
            class="text-sm"
            :class="{
              'text-green-600': item.status === 'SIGNAL_POSITIVE',
              'text-yellow-600': item.status === 'SIGNAL_NEUTRAL',
            }"
          >
            {{ item.status }}
          </p>
        </div>

        <!-- Lista de habilidades -->
        <div class="pl-6 border-l-2 border-gray-200">
          <p
            v-for="skill in item.skills"
            :key="skill"
            class="text-sm text-gray-700 mb-1"
          >
            {{ skill }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
