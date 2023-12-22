<script setup lang="ts">
import { ref, onMounted } from "vue";
import BathwMap from "../components/BathwMap.vue";
import type { Dataset } from "../types/Dataset";
import type { Bathw } from "../types/Bathw";
const bathwData = ref([] as Bathw[]);
const year = ref(2022);
let cachedData: { [index: number]: Bathw[] } = {};
function getData() {
	if (cachedData[year.value]) {
		bathwData.value = cachedData[year.value];
	} else {
		fetch(import.meta.env.VITE_API_URL + "/bathw/?year=" + year.value)
			.then((response) => response.json())
			.then(async (json) => {
				cachedData[year.value] = json;
				bathwData.value = json;
			});
	}
}
onMounted(() => {
	getData();
});
</script>
<template>
	<div class="container">
		<span>Anno:</span><br />
		<input
			v-model="year"
			type="range"
			min="1990"
			:max="new Date().getFullYear()"
			step="1"
			@change="getData"
		/>
		<h3>Mappa della qualità delle acque balneari per l'anno {{ year }}</h3>
		<BathwMap :data="bathwData" />
	</div>
</template>
