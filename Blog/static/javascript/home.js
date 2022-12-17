var element = document.getElementById('mobile--navigation')
function ToggleMobileNavigation(){
    if (element.classList.contains('mobile--navigation--open')){
        element.classList.remove('mobile--navigation--open');
    }
    else{
        element.classList.add('mobile--navigation--open');
    }
}


let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
}    
  
  slides[slideIndex-1].style.display = "block";  
  
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}



function handleReply(response_id) {
  const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
  if (reply_form_container) {
      reply_form_container.style.display = 'block';
  }
}

function handleCancel(response_id) {
  const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
  if (reply_form_container) {
      reply_form_container.style.display = 'none';
  }
}