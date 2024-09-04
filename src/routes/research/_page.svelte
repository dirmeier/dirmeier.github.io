<script>
    import papers from './papers.json';
</script>

<div id="research" style="margin-top: 1%; margin-bottom: 5%">
    <div style="margin-bottom: 1%">
        <h6>Research</h6>
        <p>
            All of papers and preprints can be found on
            <a href="https://scholar.google.de/citations?hl=en&user=v7WygEAAAAAJ&view_op=list_works&sortby=pubdate">Google Scholar</a>
            Some recent work is shown below.
        </p>
    </div>
    <div>
        {#each papers as entry, i}
            <div class="columns" style="font-size: 0.8em">
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
