<script>
	import Fa from 'svelte-fa/src/fa.svelte';
	import { faEnvelope } from '@fortawesome/free-solid-svg-icons';
</script>

<div id="about" style="margin-top: 1%; margin-bottom: 5%">
	<h6>Hello!</h6>
	<p>
		My name is Simon. I am currently working as a senior data/research scientist at the
		<a href="https://www.datascience.ch/people/simon-dirmeier">Swiss Data Science Center</a> in the
		academic cell. You can find my publications on
		<a
			href="https://scholar.google.com/citations?hl=en&user=v7WygEAAAAAJ&view_op=list_works&sortby=pubdate"
			>Google Scholar</a
		>, my software on <a href="https://github.com/dirmeier">GitHub</a>, and my CV on
		<a href="https://linkedin.com/in/simon-dirmeier">LinkedIn</a>. If you want to chat, you can
		reach me here:
		<a href="mailto:simon dot dirmeier @ protonmail com" style="color: black; margin-left: 10px;">
			<Fa icon={faEnvelope} size="1.3x" />
		</a>
	</p>
</div>
