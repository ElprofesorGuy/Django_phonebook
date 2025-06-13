const nav_button = document.querySelector('.menu-button');
const nav_list = document.querySelector('#main_nav_elements');
const menu_entrees = document.querySelector('.menu-entrees');
nav_button.addEventListener('click', function(event){
    console.log("bouton appuyée");
    nav_list.classList.toggle('sidebar');
    menu_entrees.classList.toggle('open_nav_bar');
})

