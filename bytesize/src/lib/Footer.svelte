<script lang="ts">
    if(window.matchMedia){
        const query = window.matchMedia("prefers-color-scheme:dark");
    }
    
</script>

<div class="footer-wrapper">

    <a target="_blank" rel="nofollow noopener noreferrer" href="https://discord.gg/EzDpNPDxbV"><img src="discord.svg" alt="Discord Link"></a>
    <a target="_blank" rel="nofollow noopener noreferrer" href = "https://www.instagram.com/bytesizenewsletter/"><img src="instagram.svg" alt="Instagram Link"></a>
</div>




<style>

    .footer-wrapper {
        height: 50px;
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        flex: 1;
        gap: 1rem;
    }

    a{
        transition: opacity 200ms ease-in-out,transform 200ms ease-in-out;
    }

    a:hover {
        opacity: 0.6;
        transform: scale(1.125);
    }

    

   
</style>