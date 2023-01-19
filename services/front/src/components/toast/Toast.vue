<script setup>
import { onMounted } from "vue";
import Icon from "../icons/Icon.vue";
import { ref } from "vue";

const toast = ref();
const closedEventLabel = "hidden.bs.toast";
const emit = defineEmits(["kill"]);

const props = defineProps({
  color: String,
  num: String,
  error: Boolean,
  date: Date,
});

const dateLabel = () => {
  return (
    "" +
    ("0" + props.date.getHours()).slice(-2) +
    ":" +
    ("0" + props.date.getMinutes()).slice(-2) +
    ":" +
    ("0" + props.date.getSeconds()).slice(-2)
  );
};

const kill = () => {
  emit("kill");
};

onMounted(() => {
  new bootstrap.Toast(toast.value).show();
});
</script>

<template>
  <div class="toast" ref="toast" v-on:[closedEventLabel]="kill">
    <div class="toast-header">
      <Icon :color="props.color"></Icon>
      <strong
        class="me-auto"
        :class="{ 'toast-header-sucess': props.error == false }"
        >Event notification</strong
      >
      <small class="text-muted">{{ dateLabel() }}</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
    </div>
    <div class="toast-body">
      <template v-if="props.error == false">
        Successfully created <b>{{ props.num }}</b> {{ props.color }} events
      </template>
      <template v-else> An error has occured </template>
    </div>
  </div>
</template>

<style scoped>
.toast-header-sucess {
  text-align: right;
  padding-left: 1em;
}
</style>
