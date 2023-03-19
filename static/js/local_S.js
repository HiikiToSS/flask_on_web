function turn_night_on(){
    if (localStorage.getItem('theme') == "true"){
        localStorage.setItem('theme', "false")
    }
    else{
        localStorage.setItem('theme', "true")
    }
    document.location.reload()
}