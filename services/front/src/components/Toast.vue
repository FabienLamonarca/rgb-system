<script setup>
import { toasts } from "./Toast";
const items = toasts.getItems();
</script>

<template>
  <!-- <ul>
    <li v-for="(item, index) in items">{{ item }} --- {{ index }}</li>
  </ul> -->

  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div
      v-for="(toast, index) in items"
      id="liveToast"
      class="toast show"
      :class="[
        toast.color === 'blue' && 'text-bg-primary',
        toast.color === 'red' && 'text-bg-danger',
        toast.color === 'green' && 'text-bg-success',
      ]"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-body d-flex justify-content-between">
        <span v-if="toast.error">An error has occured!</span>
        {{ toast.num }}
        <button
          @click="toasts.removeToast(index)"
          type="button"
          class="btn-close"
          aria-label="Close"
        />
      </div>
    </div>
  </div>
</template>
