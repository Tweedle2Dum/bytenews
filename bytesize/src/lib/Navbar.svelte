
<nav>
    <h1 class="logo">ByteSize</h1>
    <ul>
        <li><a href="">Advertise</a></li>
        <li><a href="">Privacy</a></li>

    </ul>
</nav>






<style>

    *{
        margin: 0;
        letter-spacing: 1px;
    }

    nav{
        padding: 1rem;
        height: 100px;
        background-color: transparent;
        display: flex;
        align-items: center;
       
        
    }

   .logo{
    font-weight: 900;
    font-size: 2rem;
    }

    ul{
        list-style: none;
        margin-left: auto;
        padding: 0;
    }

    a {
        color: var(--clr-text);
        text-decoration: none;


    }

    a:link{
        color: var(--clr-txt);
    }

    a:hover{
        text-decoration: underline;
    }


    @media (min-width:450px){
        ul {
            display: flex;
            gap: 1em;
            justify-content: center;
        }
    }
</style>