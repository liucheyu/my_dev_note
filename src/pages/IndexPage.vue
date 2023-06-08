<template>
  <q-markdown :src="mdText" show-copy no-heading-anchor-links />
</template>

<script setup lang="ts">
//import ExampleComponent from 'components/ExampleComponent.vue';
//import { ref } from 'vue';

//import { onMounted } from 'vue';

//import test from 'assets/md/programing_language/java/test.md';
const props = defineProps({
  mdText: String,
});
</script>
