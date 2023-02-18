<script lang="ts">
    import Privacy , {modalShow} from "./Privacy.svelte";

  
</script>

<nav>
  <h1 class="logo">ByteSize</h1>
  <ul>
    <li class="advertise"><a href="#!">Advertise</a></li>
    <li class="privacy"><a tabindex="0" on:click|preventDefault={modalShow} id="showmodal" href="#!">Privacy</a></li>
  </ul>
</nav>

<style>
  * {
    margin: 0;
    letter-spacing: 1px;
  }

  nav {
    padding: 1rem;
    min-height: 100px;
    background-color: transparent;
    display: flex;
    align-items: center;
  }

  /* use with advert 

    ul > li {
        
        padding: 0 0 0.5em 0;
    }

    */

  .logo {
    font-weight: 900;
    font-size: 2rem;
  }

  ul {
    list-style: none;
    margin-left: auto;
    padding: 0;
  }

  a {
    display: inline-block;
    color: var(--clr-text);
    text-decoration: underline;
    transition: transform 200ms ease-in-out;
  }
  /* remove for advert link */
  .advertise {
    display: none;
  }
  /*--- till here ---- */
  a:link {
    color: var(--clr-text);
  }
  a:visited{
    color: var(--clr-text);


  }

  a:hover {
    transform: scale(1.1);
  }
  a:active {
    transform: scale(1.1);
  }

  @media (min-width: 450px) {
    ul {
      display: flex;
      gap: 1em;
      justify-content: center;
    }
  }

  @media (min-width:600px) {
    nav {
        padding: 1rem calc(2rem + 5vw);
    }
  }
</style>
