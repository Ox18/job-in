<template>
  <div
    :style="{ width: size + 'px', height: size + 'px' }"
    class="rounded-full overflow-hidden border-2 border-gray-200 flex items-center justify-center"
  >
    <img
      :src="src"
      alt="Logo"
      :style="{ width: imageSize + 'px', height: imageSize + 'px' }"
      class="object-contain"
    />
  </div>
</template>

<script>
export default {
  name: "BubleComponent",
  props: {
    src: {
      type: String,
      required: true,
    },
  },
  data() {
    // Genera un tamaño aleatorio entre 10 y 24 para el contenedor
    // const containerSize = Math.floor(Math.random() * (24 - 10 + 1)) + 90;
    // const containerSize = 90
    // random 70 - 120
    const min = 90;
    const max = 100;
    const containerSize = Math.floor(Math.random() * (max - min + 1)) + min;
    // Calcula el tamaño de la imagen como un 70% del tamaño del contenedor
    const imageSize = Math.floor(containerSize * 20);

    return {
      size: containerSize,
      imageSize: imageSize,
    };
  },
};
</script>
