<script>
	import Fa from 'svelte-fa/src/fa.svelte';
	import { faGithub } from '@fortawesome/free-brands-svg-icons';
	import code from './code.json';
	import contr from './contributed.json';

	function getLogo(language) {
		return '/logos/' + language + '_logo.svg';
	}
</script>

<div>
	<div class="columns">
		<div class="column is-11">
			<div>
				<h3 style="font-size: 1.6em; margin-bottom: 5%">a selection of packages I developed</h3>
				<ul style="list-style: none;">
					{#each code as entry, i}
						<li style="list-style: none">
							<p>
								<img src={getLogo(entry.lang)} width="15" height="15" alt="None" />
								<a href={entry.link}> <span style="font-family: monospace">{entry.name}</span></a>
								{@html entry.description}.
							</p>
						</li>
					{/each}
				</ul>
			</div>
			<div style="padding-left: 5px; margin-top: 2%">
				<p>
					<b>You can find more on my <a href="https://github.com/dirmeier">GitHub</a> profile </b>
					<a href="https://github.com/dirmeier" style="color: black;">
						<Fa icon={faGithub} size="1.3x" />
					</a>
				</p>
			</div>
			<div>
				<h3 style="font-size: 1.6em; margin-top: 10%; margin-bottom: 5%">
					a selection of packages I like to contribute code to and/or co-develop
				</h3>
				<ul>
					{#each contr as entry, i}
						<li style="list-style: none">
							<p>
								<img src={getLogo(entry.lang)} width="15" height="15" alt="None"/>
								<a href={entry.link}> <span style="font-family: monospace">{entry.name}</span></a>
								{@html entry.description}.
							</p>
						</li>
					{/each}
				</ul>
			</div>
		</div>
	</div>
</div>
