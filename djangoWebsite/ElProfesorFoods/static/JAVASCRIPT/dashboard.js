const links = [...document.querySelectorAll('.sidebar_links li a')];
var active_link = document.querySelector('.active');
links.forEach((link)=>{
    link.addEventListener('click', (e)=>{
        console.log("contenu du lien : "+link.textContent);
        active_link.firstChild.style.color ="black";
        active_link.classList.remove('active');
        active_link = link.parentNode;
        active_link.classList.add('active');
        active_link.firstChild.style.color = "white";
    })
})