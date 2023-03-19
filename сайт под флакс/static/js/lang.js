let lang_theme = document.getElementById("switch_lang")

if (localStorage.getItem('theme') == "true"){
    lang_theme.href = '../static/dark-theme/dark-language.css'
}

else{
    lang_theme.href = '../static/css/language.css'
}