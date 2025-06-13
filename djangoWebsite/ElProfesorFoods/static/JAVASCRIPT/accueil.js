const nav_list = document.querySelector('#main_nav_elements');
const carrousel = document.querySelector(".carrousel");
const slides = [...document.querySelectorAll(".slide")];
const nav_button = document.querySelector('.menu-button');
const background = document.querySelector('.background-image');
var currentIndex = 0;

function nextSlide(){
    slides[currentIndex].classList.remove("active");
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add('active');
}
setInterval(nextSlide, 6000);
nav_button.addEventListener('click', function(event){
    nav_list.classList.toggle('mobile-menu');
    nav_list.classList.toggle('sidebar');
    /*background.classList.toggle('open_nav_bar');*/
    nav_button.classList.toggle('sidebar_button');
});

