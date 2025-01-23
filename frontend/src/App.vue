<script setup>
import { onMounted, ref } from 'vue';

let user_families = ref([]);
const backend_uri = 'http://localhost:8000'
const get_user_families_uri = `${backend_uri}/families`;
const add_family_uri = '#' //`${backend_uri}/families/add`;


onMounted(async () => {
  try {
    const response = await fetch(get_user_families_uri);
    const data = await response.json()
    user_families.value = data
  } catch (error) {
    console.log('Error fetching members')
  }
});
</script>

<template>
  <div v-if="user_families.length != 0">
    <ul>
      <li v-for="family in user_families" :key="family">
        <h4><a href="#">{{ family.name }}</a></h4>
        <span>{{ family.description }}</span>
      </li>
    </ul>
  </div>
  <div v-else>
    <h4>
      Wygląda, że nie masz dodanej żadnej rodziny.
    </h4>
  </div>
  <a :href="add_family_uri">Dodaj nową rodzinę!</a>
</template>
