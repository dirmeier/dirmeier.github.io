<script>
    import blog_2022 from './2022-blogentries.json';
    import blog_2021 from './2021-blogentries.json';
    import blog_2020 from './2020-blogentries.json';
    import blog_2019 from './2019-blogentries.json';
    import blog_2018 from './2018-blogentries.json';

    let items = [
        {date: '2022', posts: blog_2022},
        {date: '2021', posts: blog_2021},
        {date: '2020', posts: blog_2020},
        {date: '2019', posts: blog_2019},
        {date: '2018', posts: blog_2018}
    ];

    function getLogo(language) {
        return '/logos/' + language + '_logo.svg';
    }
</script>

<div>
    {#each items as item}
        <div>
            <h4>{item.date}</h4>
        </div>
        {#each item.posts as entry, i}
            <div class="columns">
                <div class="column is-3">{entry.date}</div>
                <div class="column is-9">
                    <h5>
                        {entry.title}
                        {#if entry.language}
                            <img src={getLogo(entry.language)} width="20" height="20"/>
                        {/if}
                    </h5>
                    {entry.description}
                    ({#each entry.links as link, j}<span><a href={link.link} style="display: inline">{link.name.replace("/^\\s+|\\s+$/gm", "")}</a>{#if j + 1 < entry.links.length}<span>, </span>{/if}</span>{/each}).
                </div>
            </div>
        {/each}
    {/each}
</div>