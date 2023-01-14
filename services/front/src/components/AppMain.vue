<script setup>
import EventItem from "./EventItem.vue";
import IconRed from "./icons/IconRed.vue";
import IconGreen from "./icons/IconGreen.vue";
import IconBlue from "./icons/IconBlue.vue";
import { ref } from "vue";

const toasts = ref([]);

const closeToast = (toastIndex) => {
  toasts.value.slice(toastIndex, 1);
}

const createToast = ({ color, num }, error = false) => {
  toasts.value.push({
    error,
    color,
    num,
    date: new Date()
  });
}

</script>

<template>
  <EventItem color="red" num="500" @request-success="(values) => createToast(values)"
    @request-error="(values) => createToast(values, true)">
    <template #icon>
      <IconRed />
    </template>
    <template #heading>Red event</template>
    <template #text>
      Lorem ipsum dolor sit amet, consectetur
      <a href="" target="none" rel="noopener">adipiscing</a>
      elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    </template>
  </EventItem>

  <EventItem color="green" num="100" @request-success="(values) => createToast(values)"
    @request-error="(values) => createToast(values, true)">
    <template #icon>
      <IconGreen />
    </template>
    <template #heading>Green event</template>
    <template #text>
      Ut enim ad minim veniam, quis nostrud
      <a href="" target="none" rel="noopener">exercitation</a>
      ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </template>
  </EventItem>

  <EventItem color="blue" num="3" @request-success="(values) => createToast(values)"
    @request-error="(values) => createToast(values, true)">
    <template #icon>
      <IconBlue />
    </template>
    <template #heading>Blue event</template>
    <template #text>
      Duis aute irure dolor in
      <a href="" target="none" rel="noopener">reprehenderit</a>
      in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    </template>
  </EventItem>
  <div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div v-for="(toast, index) in toasts" id="liveToast" class="toast show" :class="[toast.color === 'blue'
    && 'text-bg-primary', toast.color === 'red' && 'text-bg-danger', toast.color === 'green' && 'text-bg-success']"
      role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-body d-flex justify-content-between">
        {{ toast.num }} <span v-if="toast.error">An error has occured!</span>
        <button @click="closeToast(index)" type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" />
      </div>
    </div>
  </div>
</template>
