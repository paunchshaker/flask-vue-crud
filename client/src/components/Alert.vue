<template>
  <div>
    <v-alert type="success" show>{{ message }}</v-alert>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
