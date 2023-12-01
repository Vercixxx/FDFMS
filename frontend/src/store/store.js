import { ref, watch } from 'vue'

export const drawer = ref(false)

export const closeDrawer = () => {
  drawer.value = false
}
