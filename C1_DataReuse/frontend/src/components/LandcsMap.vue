<script setup lang="ts">
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LPolygon, LPopup } from "@vue-leaflet/vue-leaflet";
import type { Landcs } from "../types/Landcs";
const props = defineProps<{
	data: Landcs[];
	max: number;
}>();
</script>
<template>
	<div style="height: 600px; width: 800px">
		<l-map ref="map" :zoom="5" :center="[42, 12]" :useGlobalLeaflet="false">
			<l-tile-layer
				url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
				layer-type="base"
				name="OpenStreetMap"
			></l-tile-layer>
			<template v-for="comune in data">
				<l-polygon
					fillColor="#ff0000"
					:fillOpacity="
						(Number(comune.percentuale) / max) * 0.7 + 0.4
					"
					:stroke="false"
					:latLngs="comune.latLngs"
				>
					<l-popup>
						<b>{{ comune.comune }}</b
						>: {{ Math.round(Number(comune.percentuale)) }}%
					</l-popup>
				</l-polygon>
			</template>
		</l-map>
	</div>
</template>
