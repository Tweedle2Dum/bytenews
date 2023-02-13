<div class="circle one" />
<div class="circle two" />


<style>
  .circle{
    width: 800px;
    height: 800px;
    border-radius: 100%;
    background-image: linear-gradient(to right, #0f0c29, #302b63, #24243e);
    position: fixed;
    z-index: -1;
    filter: blur(100px);
    animation: rotate 50s linear  infinite alternate ;
  }


  @keyframes rotate {


   
    100%{
      transform: rotate(-360deg);
    }
    
  }


  .one {
    bottom:0% ;
    right: 25%;
    transform: translate(50%,50%);
  }

  .two {
    transform: translate(-50%,-50%);

  }

  
</style>
