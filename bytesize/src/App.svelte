<script lang="ts">
  import Gradient from "./lib/Gradient.svelte";
import Navbar from "./lib/Navbar.svelte";
  import Privacy from "./lib/Privacy.svelte";
  import Subscribe from "./lib/Subscribe.svelte";

</script>

<header><Navbar/></header>
<main>
  <Subscribe/>
  <Privacy/>
</main>

<Gradient/>
  


<style>

  main {
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 1;
  }
  
</style>