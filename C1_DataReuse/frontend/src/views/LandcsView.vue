<script setup lang="ts">
import { ref, onMounted } from "vue";
import LandcsMap from "../components/LandcsMap.vue";
import type { Dataset } from "../types/Dataset";
import type { Regione } from "../types/Regione";
import type { Landcs } from "../types/Landcs";
const landcsData = ref([] as Landcs[]);
const year = ref(2012);
const region = ref("");
const regioni = ref([] as string[]);
const maxPercentuale = ref(0);
function getData() {
	fetch(import.meta.env.VITE_API_URL + "/regioni")
		.then((response) => response.json())
		.then((json: Regione[]) => {
			regioni.value = json.map((e) => e.nomeregione);
		});
	fetch(
		import.meta.env.VITE_API_URL +
			"/landcs/?year=" +
			year.value +
			"&region=" +
			region.value,
	)
		.then((response) => response.json())
		.then((json: Landcs[]) => {
			for (let i = 0; i < json.length; i++) {
				json[i].latLngs = json[i].poly
					.replace("POLYGON ((", "")
					.replace("))", "")
					.split(", ")
					.map((e) => {
						let coords = e.split(" ");
						return [Number(coords[1]), Number(coords[0])];
					})
					.filter((point) => point[1] && point[0]);
				if (Number(json[i].percentuale) > maxPercentuale.value) {
					maxPercentuale.value = Number(json[i].percentuale);
				}
			}
			landcsData.value = json;
		});
}
onMounted(() => {
	getData();
});
</script>
<template>
	<div class="container">
		<div class="select-wrapper" style="margin-top: 2em">
			<label for="defaultSelect">Regione:</label>
			<select id="defaultSelect" v-model="region" @change="getData">
				<option value="">Scegli un'opzione</option>
				<option v-for="regione in regioni" :value="regione">
					{{ regione }}
				</option>
			</select>
		</div>
		<span>Anno:</span><br />
		<input
			v-model="year"
			type="range"
			min="1990"
			:max="new Date().getFullYear()"
			step="1"
			@change="getData"
		/>
		<h3 v-if="region">
			Mappa del consumo di suolo della regione {{ region }} per l'anno
			{{ year }}
		</h3>
		<LandcsMap :data="landcsData" :max="maxPercentuale" />
	</div>
</template>
