<script setup>
import { ref } from "vue";
import axios from "axios";

import { inject } from "vue";
import { toasts } from "./toast/Toast";

const api = inject("apiHost") + ":" + inject("apiPort");
const apiEventEndpoint = "event";

const props = defineProps({
  color: {
    type: String,
    required: true,
  },
  num: {
    type: String,
    required: true,
  },
});

const num = ref(props.num);
const color = ref(props.color);
const errorState = ref(false);
const successState = ref(false);
const loadingState = ref(false);

function submitItem() {
  loadingState.value = true;
  axios
    .post(`${api}/${apiEventEndpoint}`, {
      color: color.value,
      count: num.value,
    })
    .then((response) => {
      errorState.value = false;
      successState.value = true;
      toasts.addToast(color.value, num.value);
    })
    .catch((error) => {
      successState.value = false;
      errorState.value = true;
      toasts.addToast(null, null, true);
    })
    .finally(() => {
      loadingState.value = false;
    });
}
</script>

<template>
  <div class="item">
    <i class="vue">
      <slot name="icon"></slot>
    </i>
    <div class="details">
      <h3>
        <slot name="heading"></slot>
      </h3>
      <div class="text">
        <slot name="text"></slot>
      </div>
      <div class="input-group mb-2">
        <input
          v-model="num"
          type="text"
          class="form-control"
          aria-describedby="button-addon"
          :class="{
            'is-invalid': errorState,
          }"
        />
        <button
          @click="submitItem"
          class="btn btn-outline-secondary"
          :class="{
            'btn-outline-danger': errorState,
          }"
          type="button"
          id="button-addon"
        >
          Send&nbsp;
          <span
            class="spinner-border spinner-border-sm"
            role="status"
            aria-hidden="true"
            v-show="loadingState"
          ></span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
}

.details {
  flex: 1;
  margin-left: 1rem;
}

.text {
  margin-bottom: 0.5rem;
}

i.vue {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px;

  color: var(--color-text);
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0;
    padding: 0.4rem 0 1rem calc(var(--section-gap) / 2);
  }

  i.vue {
    top: calc(50% - 25px);
    left: -26px;
    position: absolute;
    border: 1px solid var(--color-border);
    background: var(--color-background);
    border-radius: 8px;
    width: 50px;
    height: 50px;
  }

  .item:before {
    content: " ";
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:after {
    content: " ";
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}
</style>
