const nav_button = document.querySelector('.menu-button');
const nav_list = document.querySelector('#main_nav_elements');
nav_button.addEventListener('click', function(event){
    nav_list.classList.toggle('mobile-menu');
    nav_list.classList.toggle('sidebar');
    menu_entrees.classList.toggle('open_nav_bar');
})

