<script>
	import Head from './_heads.svelte';
	import Intro from './_intro.svelte';
	import Navv from './_navbar.svelte';
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div>
	<Navv />
	<div>
		<section class="section" style="margin-top: 10%" id="home">
			<div class="container">
				<div class="columns">
					<div class="column is-offset-3 is-6">
						<Head />
						<Intro />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
