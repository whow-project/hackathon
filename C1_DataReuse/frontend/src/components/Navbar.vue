<script setup lang="ts"></script>
<template>
	<header class="it-header-wrapper">
		<div class="it-nav-wrapper">
			<div class="it-header-center-wrapper">
				<div class="container">
					<div class="row">
						<div class="col-12">
							<div class="it-header-center-content-wrapper">
								<div class="it-brand-wrapper">
									<a href="#">
										<img
											class="icon"
											aria-hidden="true"
											src="https://www.isprambiente.gov.it/++theme++ispra.theme/dist/assets/img/loghi/ispra-logo-bianco.svg"
											style="width: 300px"
										/>
										<div class="it-brand-text">
											<div class="it-brand-title">
												ISPRA maps
											</div>
											<div
												class="it-brand-tagline d-none d-md-block"
											>
												Le mappe dell'ISPRA
											</div>
										</div>
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="it-header-navbar-wrapper">
				<div class="container">
					<div class="row">
						<div class="col-12">
							<!--start nav-->
							<nav
								class="navbar navbar-expand-lg has-megamenu"
								aria-label="Navigazione principale"
							>
								<button
									class="custom-navbar-toggler"
									type="button"
									aria-controls="navC1"
									aria-expanded="false"
									aria-label="Mostra/Nascondi la navigazione"
									data-bs-toggle="navbarcollapsible"
									data-bs-target="#navC1"
								>
									<svg class="icon">
										<use
											href="/bootstrap-italia/dist/svg/sprites.svg#it-burger"
										></use>
									</svg>
								</button>
								<div
									class="navbar-collapsable"
									id="navC1"
									style="display: none"
								>
									<div
										class="overlay"
										style="display: none"
									></div>
									<div class="close-div">
										<button
											class="btn close-menu"
											type="button"
										>
											<span class="visually-hidden"
												>Nascondi la navigazione</span
											>
											<svg class="icon">
												<use
													href="/bootstrap-italia/dist/svg/sprites.svg#it-close-big"
												></use>
											</svg>
										</button>
									</div>
									<div class="menu-wrapper">
										<ul class="navbar-nav">
											<li class="nav-item">
												<a
													class="nav-link"
													href="/bathw"
													><span
														>Acque di
														balneazione</span
													></a
												>
											</li>
											<li class="nav-item">
												<a
													class="nav-link"
													href="/landcs"
													><span
														>Consumo suolo</span
													></a
												>
											</li>
										</ul>
									</div>
								</div>
							</nav>
						</div>
					</div>
				</div>
			</div>
		</div>
	</header>
</template>
