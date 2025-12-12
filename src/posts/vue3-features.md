# Exploring Vue 3 Features

Vue 3 brings many exciting features and improvements over Vue 2. Let's explore some of the key features.

## Composition API

The Composition API is one of the most significant additions to Vue 3. It provides a new way to organize component logic:

```javascript
import { ref, computed, onMounted } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const doubleCount = computed(() => count.value * 2)
    
    onMounted(() => {
      console.log('Component mounted!')
    })
    
    return { count, doubleCount }
  }
}
```

## Better Performance

Vue 3 offers improved performance with:
- Faster virtual DOM
- More efficient reactivity system
- Smaller bundle size

## Teleport Component

The new `<Teleport>` component allows you to render content in a different part of the DOM:

```vue
<Teleport to="body">
  <div class="modal">
    Modal content here
  </div>
</Teleport>
```

## Multiple Root Elements

Components can now have multiple root elements without a wrapper:

```vue
<template>
  <header>Header</header>
  <main>Content</main>
  <footer>Footer</footer>
</template>
```

## Conclusion

Vue 3 is a powerful framework that makes building modern web applications easier and more efficient.
