<script setup>
import { toasts } from "./Toast";
import Toast from "./Toast.vue";

const items = toasts.getItems();

const removeToast = (itemToDelete) => {
  console.log(itemToDelete.uuid);
  items.value.splice(
    items.value.findIndex((item) => item.uuid === itemToDelete.uuid),
    1
  );
};
</script>

<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <template v-for="item in items" :key="item.uuid">
      <Toast
        :uuid="item.uuid"
        :color="item.color"
        :num="item.num"
        :error="item.error"
        :date="item.date"
        v-on:kill="removeToast(item)"
      ></Toast>
    </template>
  </div>
</template>
