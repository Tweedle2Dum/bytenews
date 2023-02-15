<script lang="ts">
  import {onMount} from 'svelte';
  import { detach } from "svelte/internal";
  import { get } from "svelte/store";
  import Privacy from './Privacy.svelte';
  const URL = "https://bytenewsbackend.fly.dev/create";
  let msg;
  onMount(()=>{
    msg = document.querySelector(".msg"); 
  })
  function handleSubmit(event) {
    const formData = new FormData(event.target);
    const userEmail = Object.fromEntries(formData.entries());
    console.log(JSON.stringify(userEmail));
    fetch(`${URL}`, {
      method: "POST",
      body: JSON.stringify(userEmail),
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response)=>{
        return response.json();
    })
    .then((response) => {
      console.log(response.status_code)
      if(response.status_code >=200 && response.status_code<300){
        msg.textContent = "You have been sucessfully subscribed!"

      }
      else if(response.status_code==400) {
        msg.textContent = "Already subscribed!"

      }
      else {
        msg.textContent = "Some error occured, try again later.."
      }
    });
  }
  
  
  
</script>

<div class="subscribe">
  <p>
    Keep pace with cutting-edge tech advancements through a AI-powered
    Byte-sized Newsletter, delivering concise updates right to your inbox.
  </p>

  <form on:submit|preventDefault={handleSubmit}>
    <div class="label-input-wrapper">
      <label for="email">Email:</label>
      <input
        type="email"
        name="email"
        required
        aria-required="true"
        autofocus
        placeholder="Email Address"
      />
    </div>
    <span class="msg" />
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
    box-shadow: 0 0 14px rgba(0, 0, 0, 0.3);
    border-radius: 12px;
  }

  form {
    display: flex;
    flex-flow: column wrap;
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
    background-color: rgba(255, 255, 255, 0.8);
  }

  input::placeholder {
    letter-spacing: 1px;
    font-size: 1rem;
  }

  .label-input-wrapper {
    width: 100%;
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    gap: 1em;
  }

  .msg{
    position: relative;
    font-size: 0.8rem;
  }

  .btn-wrapper {
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
