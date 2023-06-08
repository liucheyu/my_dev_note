<template>
  <router-view />
</template>

<script setup lang="ts">
import { useMdPathStore } from 'stores/mdPath';
const MdPath = useMdPathStore();
const { updateMdPath } = MdPath;

fetch('/mdFiles.json')
  .then((res) => {
    return res.json();
  })
  .then((res) => updateMdPath(res));
</script>
