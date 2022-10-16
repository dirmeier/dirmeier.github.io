<script>
	import blog_2022 from './2022-blogentries.json';
	import blog_2021 from './2021-blogentries.json';
	import blog_2020 from './2020-blogentries.json';
	import blog_2019 from './2019-blogentries.json';
	import blog_2018 from './2018-blogentries.json';

	let items = [
		{ date: '2022', posts: blog_2022 },
		{ date: '2021', posts: blog_2021 },
		{ date: '2020', posts: blog_2020 },
		{ date: '2019', posts: blog_2019 },
		{ date: '2018', posts: blog_2018 }
	];

	function getLogo(language) {
		return '/logos/' + language + '_logo.svg';
	}
</script>

<div>
	<h2>Case studies</h2>
	<p>
		Below you can find a collection of case studies and notebooks on topics I work on or am
		interested in. Topics revolve generally around probabilistic modelling, ranging from
		probabilistic machine and deep learning, to Bayesian statistics, to causal inference. The case
		studies mainly use the probabilistic programming languages Stan, TensorFlow Probability and
		NumPyro.
	</p>

	{#each items as item}
		<div>
			<h4>{item.date}</h4>
		</div>
		{#each item.posts as entry, i}
			<div class="columns">
				<div class="column is-3">{entry.date}</div>
				<div class="column is-9">
					<h6>
						{entry.title}
						{#if entry.language}
							<img src={getLogo(entry.language)} width="20" height="20" />
						{/if}
					</h6>
					{entry.description}
					{#each entry.links as link, j}
						(<span>
							<a href={link.link} style="display: inline">{link.name}</a>
							{#if j + 1 < entry.links.length}
								<span>, </span>
							{/if}
						</span>)
					{/each}
				</div>
			</div>
		{/each}
	{/each}
</div>
