var login = document.querySelector('input[type="submit"]');
var form_section = document.querySelector('.body');
var message = document.querySelector('#message');
var close = document.querySelector('.close');
var valid_section = document.querySelector('.valid-message');
const nav_button = document.querySelector('.menu-button');
const nav_list = document.querySelector('#main_nav_elements');
const menu_entrees = document.querySelector('.menu-entrees');
login.addEventListener("click", function(event){
    event.preventDefault();
    var checkUsername = document.querySelector('input[type="text"]');
    var checkPassword = document.querySelector('input[type="password"]');
    if(checkPassword.value === "12345" && checkUsername.value === "GUY"){
        form_section.style.display = "none";
        message.style.margin= "150px";
        message.style.background = "none";
        valid_section.style.background = "#f4f4f4";
        message.style.transition = "1s";
    }else{
        alert("Mot de passe incorrect");
    }
});
close.addEventListener("click", function(){
    message.style.margin = "-2000px";
})
nav_button.addEventListener('click', function(event){
    nav_list.classList.toggle('mobile-menu');
    nav_list.classList.toggle('sidebar');
    menu_entrees.classList.toggle('open_nav_bar');
})

/*const links = [...document.querySelectorAll('#main_nav_elements li a')];
var active = document.querySelector('.active_link');
console.log("active link est "+active.textContent);
links.forEach((link)=>{
    link.addEventListener('click', (e)=>{
        active.classList.remove('active_link');
        active = link;
        active.classList.add('active_link');
    })
})*/