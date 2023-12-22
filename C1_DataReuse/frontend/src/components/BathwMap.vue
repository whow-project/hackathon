<script setup lang="ts">
import "leaflet/dist/leaflet.css";
import {
	LMap,
	LTileLayer,
	LCircleMarker,
	LPopup,
} from "@vue-leaflet/vue-leaflet";
import type { Bathw } from "../types/Bathw";
const props = defineProps<{
	data: Bathw[];
}>();
const qualityColor: { [index: string]: string } = {
	"Not classified": "#808080",
	Poor: "#ff0000",
	Sufficient: "#ffff00",
	"Good or Sufficient": "#ffff00",
	Good: "#77ff00",
	Excellent: "#00ff00",
};
</script>
<template>
	<div style="height: 600px; width: 800px">
		<l-map ref="map" :zoom="5" :center="[42, 12]" :useGlobalLeaflet="false">
			<l-tile-layer
				url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
				layer-type="base"
				name="OpenStreetMap"
			></l-tile-layer>
			<l-circle-marker
				v-for="point in data"
				:radius="5"
				:fillOpacity="1"
				:stroke="false"
				:color="qualityColor[point.quality]"
				:lat-lng="[point.lat, point.long]"
			>
				<l-popup>
					<b>Luogo</b>: {{ point.municipality }},
					{{ point.province }}, {{ point.region }}<br />
					<b>Qualità</b>: {{ point.quality }}
				</l-popup>
			</l-circle-marker>
		</l-map>
	</div>
</template>
