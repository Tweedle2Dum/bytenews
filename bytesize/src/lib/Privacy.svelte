<script  context="module" lang="ts">
  import Gradient from "./Gradient.svelte";

  const dialog = document.getElementsByTagName("dialog");
   export function modalShow(event){
        console.log(dialog[0])
        dialog[0].showModal();
        
   }

   const exitModal = document.querySelector(".exit");
   function closeModal(event){
    dialog[0].close()

   }
</script>

<dialog class="modal">
    <h3>Privacy and Policy-</h3>
  <h1>Introduction:</h1>
  <p>
    At Byte Size, we are committed to protecting the privacy and security of our
    subscribers. This privacy policy outlines the information we collect, how we
    use it, and how we protect it. Our newsletter does not collect any
    information except for your email address and we comply with the Children's
    Online Privacy Protection Act (COPPA) by not knowingly collecting
    information from children under the age of 13.
  </p>
  <h2>Email Collection:</h2>
  <p>
    The only information we collect is your email address when you sign up to
    receive our newsletter. This email address is used solely for the purpose of
    delivering our newsletter to you and will not be shared with third parties.
  </p>
  <h2>Sponsored Content:</h2>
  <p>
    From time to time, our newsletter may include sponsored content. However,
    such content will never be the sole purpose of the newsletter. Any sponsored
    content will be clearly marked as such and we will only work with reputable
    third parties who comply with privacy laws.
  </p>
  <h2>Information Use:</h2>
  <p>
    The email address you provide us will only be used to send you our
    newsletter, and will not be used for any other purpose. We will not share
    your email address with third parties for their marketing purposes. Data
    Security: We take the security of your data very seriously and employ
    appropriate measures to protect it from unauthorized access, use,
    disclosure, alteration or destruction.
  </p>
  <h2>Changes to Privacy Policy:</h2>
  <p>
    We may update this privacy policy from time to time to reflect changes in
    our practices or services. Any changes made will be posted on this page.
    <br><strong>Contact Us</strong>: If you have any questions or concerns about this privacy policy,
    or if you would like to request access to or correction of your information,
    please contact us by email at [insert email address here].
  </p>
  <h2>Effective Date:</h2>
  <p>This privacy policy is effective as of [insert date here].</p>
  <Gradient/>
  <span class="exit-wrapper"><button on:click|preventDefault={closeModal} class="exit">BACK</button></span>

</dialog>

<style>
  .modal {
    position: relative;
    background-color: transparent;
    color: var(--clr-text);
    padding: 2rem;
    border: 1px solid rgba(76, 36, 125, 0.771);
    height: 80%;
    width: 75%;
    letter-spacing: 1px;
    box-shadow: 0 0 14px rgba(76, 36, 125, 0.771);
    
    
  }

  .modal::backdrop{
    background-color: rgba(0, 0, 0, 1);   
  }


  .exit-wrapper {
    display: inline-block;
    background-image: linear-gradient(
      to right,
      #ff512f 0%,
      #dd2476 51%,
      #ff512f 100%
    );
    border-radius: 4px;
    padding: 1px;

  }

  .exit {
    appearance: none;
    padding: 0.7em 0.7em;
    font-size: 1.2rem;
    letter-spacing: 1px;
    border: 0px solid transparent;
    border-radius: 12px;
    background-color: transparent;
    color: var(--clr-text);
    transition: 0.5s;
  }

  .exit-wrapper:hover{
    background-image: linear-gradient(
      to right,
      #ff512f 0%,
      #dd2476 51%,
      #ff512f 100%
    );
    background-size: 200% auto;
    box-shadow: 0 0 20px orangered;
    background-position: right center; /* change the direction of the change here */
    color: #fff;
    text-decoration: none;
  }
  

  
</style>
