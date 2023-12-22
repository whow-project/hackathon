<script setup lang="ts">
import { ref, onMounted } from "vue";
import type { Dataset } from "../types/Dataset";
const datasets = ref([] as Dataset[]);
onMounted(() => {
	fetch(import.meta.env.VITE_API_URL + "/datasets/")
		.then((response) => response.json())
		.then(async (json) => {
			datasets.value = json;
		});
});
</script>

<template>
	<div>
		<div class="row">
			<div class="select-wrapper">
				<label for="defaultSelect">Dataset</label>
				<select id="defaultSelect">
					<option value="">Scegli un'opzione</option>
					<option v-for="dataset in datasets" :value="dataset.uri">
						{{ dataset.label }}
					</option>
				</select>
			</div>
		</div>
	</div>
</template>
