<script>
	import Navv from './_navbar.svelte';
	import Bottom from './_bottom.svelte';
	import About from './about/_page.svelte';
	import Research from './research/_page.svelte';
	import Software from './code/_page.svelte';
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
					<div class="column is-offset-4 is-6">
						<About/>
						<Research/>
						<Software/>
						<Bottom />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
