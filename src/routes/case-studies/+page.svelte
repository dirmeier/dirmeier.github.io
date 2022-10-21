<script>
	import Navv from '../_navbar.svelte';
	import Studies from './_case_studies.svelte';
	import Bottom from '../_bottom.svelte';
</script>

<svelte:head>
	<title>Case studies</title>
</svelte:head>

<div>
	<Navv />
	<div>
		<section class="section">
			<div class="container">
				<div class="columns">
					<div class="column is-offset-4 is-6">
						<Studies />
						<Bottom />
					</div>
				</div>
			</div>
		</section>
	</div>
</div>
