<script>
	import Navv from '../_navbar.svelte';
	import Page from './_page.svelte';
	import Bottom from '../_bottom.svelte';
</script>

<svelte:head>
	<title>code</title>
</svelte:head>

<div>
	<Navv />
	<div>
		<section class="section">
			<div class="container">
				<div class="columns">
					<div class="column is-offset-4 is-6">
						<Page />
						<Bottom />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
