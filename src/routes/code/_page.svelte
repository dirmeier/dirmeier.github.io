<script>
    import code from './code.json';
    import contr from './contributed.json';

    function getLogo(language) {
        return '/logos/' + language + '_logo.svg';
    }
</script>

<div id="code">
    <div style="margin-top: 1%; margin-bottom: 5%">
        <div style="margin-bottom: 1%">
            <h6>Software</h6>
            <p>
                My software and code is openly accessible on
                <a href="https://github.com/dirmeier">GitHub</a>. Some packages are shown below.
            </p>
        </div>
        <div  style=" font-size: 0.8em !important; margin-bottom: 1%">
            <ul style="list-style: none;">
                {#each code as entry, i}
                    <li style="list-style: none">
                        <p>
                            <img src={getLogo(entry.lang)} width="15" height="15" alt="None"/>
                            <a href={entry.link}>
                                <span style="font-family: monospace; font-size: 1rem">{entry.name}</span></a
                            >
                            {@html entry.description}.
                        </p>
                    </li>
                {/each}
            </ul>
        </div>
        <div style="margin-bottom: 1%">
            <h6>Relevant (significant) contributions</h6>
        </div>
        <div style=" font-size: 0.8em !important">
            <ul>
                {#each contr as entry, i}
                    <li style="list-style: none;">
                        <p>
                            <img src={getLogo(entry.lang)} width="15" height="15" alt="None" />
                            <a href={entry.link}>
                                <span style="font-family: monospace;">{entry.name}</span></a
                            >
                            {@html entry.description}.
                        </p>
                    </li>
                {/each}
            </ul>
        </div>
    </div>
</div>
