import { ref } from "vue";
import { reactive } from "vue";

const toastItems = ref([]);

export const toasts = reactive({
  getItems: () => {
    return toastItems;
  },
  removeToast: (index) => {
    toastItems.value.splice(index, 1);
  },
  addToast: (color, num, err = false) => {
    toastItems.value.push({
      color: color,
      num: num,
      err: err,
      date: new Date(),
    });
  },
});
