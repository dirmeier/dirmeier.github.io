<script>
    import logo from '$lib/profile.jpg';
    import Fa from "svelte-fa/src/fa.svelte"
    import {faGithub} from "@fortawesome/free-brands-svg-icons"

    function getLogo(language) {
        return '/logos/' + language + '_logo.svg';
    }
</script>
<div>
    <div>
        <h4>2022-</h4>
    </div>
    <a href="https://github.com/dirmeier" style="color: black;">
        <Fa icon={faGithub} size="1.5x"/>
    </a>
        <div class="columns">
            <div class="column is-offset-3 is-9">
                <h5>
                    reconcile

                        <img src={getLogo("Python")} width="20" height="20"/>
                </h5>
            </div>
        </div>
</div>
