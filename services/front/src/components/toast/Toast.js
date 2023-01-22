import { ref } from "vue";
import { reactive } from "vue";
import { v4 as uuidv4 } from "uuid";

const toastItems = ref([]);

export const toasts = reactive({
  getItems: () => {
    return toastItems;
  },
  removeToast: (index) => {
    toastItems.value.splice(index, 1);
  },
  addToast: (color, num, error = false) => {
    toastItems.value.push({
      uuid: uuidv4(),
      color: color,
      num: num,
      error: error,
      date: new Date(),
    });
  },
});
