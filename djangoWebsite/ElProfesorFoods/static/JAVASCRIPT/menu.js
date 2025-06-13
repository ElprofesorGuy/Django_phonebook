var add_article = [...document.querySelectorAll('.add')];
const nav_button = document.querySelector('.menu-button');
const nav_list = document.querySelector('#main_nav_elements');
const menu_entrees = document.querySelector('.menu-entrees');
var name_article = [...document.querySelectorAll('.menu-name')];

var name_article_value = [];
/*for(var i = 0, l=name_article.length; i<l;i++){
    name_article_value.push(name_article[i].textContent);
    console.log(name_article[i].textContent);
}*/
add_article.forEach((element) => {
    element.addEventListener("click", function(event){
        event.target.textContent = "Déjà dans le panier";
        element.style.background = "red";
        event.target.classList.remove("add");
    });
});
nav_button.addEventListener('click', function(event){
    nav_list.classList.toggle('mobile-menu');
    nav_list.classList.toggle('sidebar');
    menu_entrees.classList.toggle('open_nav_bar');
})
var price = [...document.querySelectorAll('.price')];
console.log("Couleur du texte est : ");
