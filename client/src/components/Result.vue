<template>
  <div class="mt-4">
    <h4 class="mb-4">Search results in order of increasing (straight line) distance in meters</h4>
    <ol>
      <transition-group name="fade" appear>
        <li v-for="item in items" :key="item.lat+item.lon" :style="{marginBottom: '1rem'}">
          <span :style="{marginLeft: '10px', fontWeight: 'bold'}">{{ item.name }}</span> is located at a distance of {{ item.dist }}m.
        </li>
      </transition-group>
    </ol>
  </div>
</template>

<script>
  export default {
    props: ['items']
  }
</script>

<style>
  .fade-enter {
    opacity: 0;
  }
  .fade-enter-active {
    transition: opacity 3s;
  }
</style>
