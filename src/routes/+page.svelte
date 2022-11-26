<script>
	import About from './_about.svelte';
	import Navv from './_navbar.svelte';
</script>

<svelte:head>
	<title>about</title>
</svelte:head>
<div>
	<Navv />
	<div>
		<section class="section">
			<div class="container">
				<div class="columns">
					<div class="column is-offset-3 is-6">
						<About />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
