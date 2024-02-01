<script>
	import papers from './papers.json';
</script>

<div id="research" style="margin-top: 1%; margin-bottom: 5%">
	<div>
		<h4>selected papers and preprints</h4>
	</div>
	<div style="padding-left: 15px">
		<div style="margin-bottom: 15px">
			<p>
				My papers and preprints can be found on
				<a
					href="https://scholar.google.de/citations?hl=en&user=v7WygEAAAAAJ&view_op=list_works&sortby=pubdate"
					>Google Scholar</a
				>. A selection is listed below.
			</p>
		</div>
		<div>
			{#each papers as entry, i}
				<div class="columns">
					<div class="column is-1">{entry.year}</div>
					<div class="column is-10">
						<div><b>{entry.title}</b></div>
						{@html entry.authors}. <i>{entry.journal}</i>, {entry.year}.
						<a href={entry.link}>doi:{entry.doi}</a>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>
