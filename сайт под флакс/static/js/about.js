let about_theme = document.getElementById("switch_about")

if (localStorage.getItem('theme') == "true"){
    about_theme.href = '../static/dark-theme/dark-about.css'
}

else{
    about_theme.href = '../static/css/about.css'
}
