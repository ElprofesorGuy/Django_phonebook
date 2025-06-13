/*var list = [...document.querySelectorAll('.navigation li')];
function activeLink(){
    list.forEach((item)=>{
        item.classList.remove('hovered');
        this.classList.add('hovered');
    })
}
list.forEach((item)=>{
    item.addEventListener('mouseover', activeLink);
})*/

var toggle = document.querySelector('.toggle');
var navigation = document.querySelector('.navigation');
var main = document.querySelector('.main');

toggle.onclick = function(){
    navigation.classList.toggle('active');
    main.classList.toggle('active');
}