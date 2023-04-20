var nav_theme = document.getElementById("switch_nav")
var day_night_text = document.getElementById("go_day_night")

var dayLink = document.getElementById("href_day")
var nightLink = document.getElementById("href_night")

if (localStorage.getItem('theme') == "true"){
    // nav_theme.href = '../css/baseStyle.css'
    nav_theme.href = dayLink.href
    if (day_night_text){day_night_text.innerHTML = 'На дневную'}
}

else{
    nav_theme.href = '../css/base.css'
    if (day_night_text){day_night_text.innerHTML = 'На ночную'}
}

function openMenu(){
    document.getElementById("sidebar").classList.toggle('active');
}