<script lang="ts">
  import { detach } from "svelte/internal";


      const URL = "https://bytenewsbackend.fly.dev/create";

    function handleSubmit(event){
        const formData = new FormData(event.target);
        const userEmail = Object.fromEntries(formData.entries());
        console.log(JSON.stringify(userEmail));
        const response = fetch(`${URL}`,{
            method:'POST',
            body: JSON.stringify(userEmail),
            headers:{
              'Content-Type': 'application/json'
            },
        })
        console.log(response);
                

    }    
</script>




<div class="subscribe">
  <p>
    Keep pace with cutting-edge tech advancements through a AI-powered
    Byte-sized Newsletter, delivering concise updates right to your inbox.
  </p>

  <form on:submit|preventDefault={handleSubmit}>
    <label for="email">Email:</label>
    <input
      type="email"
      name="email"
      required
      aria-required="true"
      autofocus
      placeholder="Email Address"
    />
    <span class="btn-wrapper"><button type="submit">Subscribe</button></span>
  </form>
</div>

<style>
  .subscribe {
    max-width: 400px;
    padding: 2rem;
    font-size: 1.2rem;
    letter-spacing: 1px;
    color: var(--clr-text);
    box-shadow: 0 0 14px rgba(0,0,0,0.3);
    border-radius: 12px;

  }

  form {
    display: flex;
    flex-flow: row wrap;
    gap: 1rem;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
  }

  input[type="email"] {
    flex: 1;
    appearance: none;
    padding: 0.5em 1em;
    border: 1px solid transparent;
    border-radius: 12px;
    background-color: rgba(255,255,255,0.8);
  }

  input::placeholder{
    letter-spacing: 1px;
    font-size: 1rem;
  }

  .btn-wrapper{
    background-image: linear-gradient(
      to right,
      #ff512f 0%,
      #dd2476 51%,
      #ff512f 100%
    );
    border-radius: 12px;
    padding: 1px;
  }

  button[type="submit"] {
    appearance: none;
    padding: 0.3em 0.7em;
    font-size: 1.2rem;
    letter-spacing: 1px;
    border: 0px solid transparent;
    border-radius: 12px;
    background-color: transparent;
    color: var(--clr-text);
    transition: 0.5s;

  }

  button[type="submit"]:hover {
    background-image: linear-gradient(
      to right,
      #ff512f 0%,
      #dd2476 51%,
      #ff512f 100%
    );
    background-size: 200% auto;
    box-shadow: 0 0 20px orangered;
    display: block;
    background-position: right center; /* change the direction of the change here */
    color: #fff;
    text-decoration: none;
  }

  p {
    text-align: center;
  }
</style>
