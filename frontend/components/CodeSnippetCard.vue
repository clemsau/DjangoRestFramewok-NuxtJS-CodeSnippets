<template>
  <div class="max-w-sm rounded overflow-hidden shadow-lg">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ snippet.name }}</div>
      <p class="text-gray-700 text-base">
        {{ snippet.code }}
      </p>
    </div>
  </div>
</template>
<script>
export default {
    name: "CodeSnippetCard"
};
</script>
<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
