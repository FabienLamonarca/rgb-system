<script setup>
import IconBlue from "../icons/IconBlue.vue";
import IconGreen from "../icons/IconGreen.vue";
import IconRed from "../icons/IconRed.vue";
const props = defineProps({
  color: String,
});
</script>

<template>
  <template v-if="props.color == 'blue'">
    <IconBlue></IconBlue>
  </template>
  <template v-if="props.color == 'green'">
    <IconGreen></IconGreen>
  </template>
  <template v-if="props.color == 'red'">
    <IconRed></IconRed>
  </template>
</template>
