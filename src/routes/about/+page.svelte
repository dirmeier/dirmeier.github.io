<script>
	import Navv from '../_navbar.svelte';
	import About from './_about.svelte';
	import Consulting from './_consulting.svelte';
	import Bottom from '../_bottom.svelte';
</script>

<svelte:head>
	<title>About</title>
</svelte:head>

<div>
	<Navv />
	<div>
		<section class="section">
			<div class="container">
				<div class="columns">
					<div class="column is-offset-4 is-6">
						<About />
						<Consulting />
						<Bottom />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
