<script>
	import Navv from './_navbar.svelte';
	import About from './about/_page.svelte';
</script>

<svelte:head>
	<title>simon dirmeier</title>
</svelte:head>

<div>
	<Navv />
	<div>
		<section class="section">
			<div class="container">
				<div class="columns">
					<div class="column is-10 is-offset-1">
						<About />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
