<script setup>
import { toasts } from "./Toast";
import Toast from "./Toast.vue";

const items = toasts.getItems();

const removeToast = (itemToDelete) => {
  items.value.splice(
    items.value.findIndex((item) => item.date === itemToDelete.date),
    1
  );
};
</script>

<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <template v-for="item in items" :key="item.date">
      <Toast
        :color="item.color"
        :num="item.num"
        :error="item.error"
        :date="item.date"
        v-on:kill="removeToast(item)"
      ></Toast>
    </template>
  </div>
</template>
