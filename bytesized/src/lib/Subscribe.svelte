<script lang="ts">

    const URL = "https://bytenewsbackend.fly.dev/create";
    function handleSubmit(event){
        const formData = new FormData(event.target);
        const userEmail = Object.fromEntries(formData.entries());
       fetch(`${URL}`,{
            method: 'POST',
            body: JSON.stringify(userEmail),
       })

    }
</script>

<main>
  <div class="wrapper">
    <h2>Bytesized - your weekly does of tech news, hacks and tips!</h2>
    <form on:submit|preventDefault={handleSubmit}>
        
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="" placeholder="Email Address"/>
            <button type="submit">Submit</button>
        
    </form>
</div>
</main>

<style>
  .wrapper {
    display: flex;
    flex-flow: column wrap;
    max-width: 800px;
    letter-spacing: 1px;
    padding: 1.5em 2em;
    background-color: #313130;
    justify-content: center;
    align-items: center;
    border-radius: 16px;
  }
  main {
    display: flex;
    flex: 1;
    flex-flow: column wrap;
    justify-content: center;
    align-items: center;
  }

  form{
    font-size: 1.4rem;
    display: flex;
    gap: 0.5em;
    align-items: center;
    justify-content: space-between;
  }

  input{
    outline: transparent;
    appearance: none;
    border: 1px solid transparent;
    padding: 0.5em;
    font-size: 1.2rem;
    border-radius: 12px;

  }

  input::placeholder {
    letter-spacing: 1px;


  }

  button {
    letter-spacing: 1px;
    appearance: none;
    padding: 0.5em 1em;
    font-size: 1.2rem;
    color: whitesmoke;
    border: 1px solid white;
    border-radius: 12px;
    background-color: #313130;
    transition: background-color 0.3s ease-in-out ;

  }

  button:hover {
    color: #313130;
    background-color: whitesmoke;

  }
</style>
