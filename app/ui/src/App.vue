<template>
  <div class="flex flex-col h-full justify-center items-center px-6">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Estilos opcionales */
nav {
  padding: 10px;
  text-align: center;
}

router-link {
  margin: 0 10px;
  text-decoration: none;
  color: #42b983;
}
</style>
