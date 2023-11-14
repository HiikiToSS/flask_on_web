let nav_theme = document.getElementById("switch_nav")
let day_night_text = document.getElementById("go_day_night")

let dayLink = document.getElementById("day_href_css")
let nightLink = document.getElementById("night_href_css")

if (localStorage.getItem('theme') == "true"){
    //nav_theme.href = '../dark-theme/navigation-dark.css'
    nav_theme.href = nightLink.href
    if (day_night_text){day_night_text.innerHTML = 'На дневную'}
}

else{
    //nav_theme.href = '../css/navigation.css'
    nav_theme.href = dayLink.href
    if (day_night_text){day_night_text.innerHTML = 'На ночную'}
}