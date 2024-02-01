<script>
    import code from './code.json';
    import contr from './contributed.json';

    function getLogo(language) {
        return '/logos/' + language + '_logo.svg';
    }
</script>

<div id="code">
    <div style="margin-top: 1%; margin-bottom: 5%">
        <div >
            <h4>selected software</h4>
        </div>
        <div style="padding-left: 15px">
            <div style="margin-bottom: 15px">
                <p>
                    My software and code is openly accessible on
                    <a href="https://github.com/dirmeier">GitHub</a>.
                    Some packages are shown below.
                </p>
            </div>
            <div>
                <ul style="list-style: none;">
                    {#each code as entry, i}
                        <li style="list-style: none">
                            <p>
                                <img src={getLogo(entry.lang)} width="15" height="15" alt="None"/>
                                <a href={entry.link}> <span
                                        style="font-family: monospace; font-size: 0.85rem">{entry.name}</span></a>
                                {@html entry.description}.
                            </p>
                        </li>
                    {/each}
                </ul>
            </div>
        </div>
    </div>
    <div style="margin-top: 1%; margin-bottom: 5%">
        <div>
            <h4>selected software I like contributing to</h4>
        </div>
        <div style="padding-left: 15px">
            <div>
                <ul>
                    {#each contr as entry, i}
                        <li style="list-style: none">
                            <p>
                                <img src={getLogo(entry.lang)} width="15" height="15" alt="None"/>
                                <a href={entry.link}> <span
                                        style="font-family: monospace;  font-size: 0.85rem">{entry.name}</span></a>
                                {@html entry.description}.
                            </p>
                        </li>
                    {/each}
                </ul>
            </div>
        </div>
    </div>
</div>

