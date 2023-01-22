<script setup>
import EventItem from "./EventItem.vue";
import Icon from "./icons/Icon.vue";
import ToastManager from "./toast/ToastManager.vue";
</script>

<template>
  <EventItem color="red" num="500">
    <template #icon>
      <Icon color="red" />
    </template>
    <template #heading>Red event</template>
    <template #text>
      Lorem ipsum dolor sit amet, consectetur
      <a href="" target="none" rel="noopener">adipiscing</a>
      elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    </template>
  </EventItem>

  <EventItem color="green" num="100">
    <template #icon>
      <Icon color="green" />
    </template>
    <template #heading>Green event</template>
    <template #text>
      Ut enim ad minim veniam, quis nostrud
      <a href="" target="none" rel="noopener">exercitation</a>
      ullamco laboris nisi ut aliquip ex ea commodo consequat.
    </template>
  </EventItem>

  <EventItem color="blue" num="3">
    <template #icon>
      <Icon color="blue" />
    </template>
    <template #heading>Blue event</template>
    <template #text>
      Duis aute irure dolor in
      <a href="" target="none" rel="noopener">reprehenderit</a>
      in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    </template>
  </EventItem>

  <ToastManager></ToastManager>
</template>
