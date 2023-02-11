<script lang="ts">

</script>

<header>
    <nav>
        <ul class="link-wrapper">
            <li class="name">BYTE SIZED</li>
            <li id="right-start"><a  href="">Privacy</a></li>
            <li><a href="">Advertise</a></li>
        </ul>
    </nav>
</header>


<style>

    nav {
        padding:0 2rem;
        font-size: 1.3rem;
        background-color: #313030;
        border-radius: 0 0 16px 16px;
    }


    .name {
        font-weight: 500;
        font-size: 2rem;
        font-family: monospace;
        word-spacing: -10px;

    }

   
    .link-wrapper{
        padding: 0;
        color: white;
        width:100%;
        display: flex;
        align-items: center;
        margin: 0;
        gap: 16px;
        height: 100px;
    }
    #right-start{
        margin-left: auto;
    }
    .link-wrapper  li{
        list-style: none;

    }

    .link-wrapper a {
        font-weight: 500;
        letter-spacing: 1px;
        color: white;
        text-decoration: none;
        border: 1px solid whitesmoke;
        padding: 0.5em 1em;
        border-radius: 12px;
        transition: background-color 0.3s ease-in-out ;
    }

             
   
         

    .link-wrapper a:hover{
        color: #313030;
        background-color: whitesmoke;
    }
    
    .link-wrapper a:active {
        color: rebeccapurple;
        opacity: 0.7;
    }

</style>