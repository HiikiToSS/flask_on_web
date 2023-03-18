let nav_theme = document.getElementById("switch_nav")
let day_night_text = document.getElementById("go_day_night")

if (localStorage.getItem('theme') == "true"){
  nav_theme.href = '../../static/dark-theme/navigation-dark.css'
  if (day_night_text){day_night_text.innerHTML = 'На дневную'}
}

else{
  nav_theme.href = '../../static/css/navigation.css'
  if (day_night_text){day_night_text.innerHTML = 'На ночную'}
}