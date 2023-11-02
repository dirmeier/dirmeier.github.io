<script>
	import papers from './papers.json';
</script>

<div>
	<div>
		<h3 style="font-size: 1.6em; margin-bottom: 5%">selected papers and preprints</h3>
	</div>

	<div style="padding-left: 15px">
		<div style="margin-bottom: 5%">
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
