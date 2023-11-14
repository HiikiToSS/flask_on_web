let contacts_theme = document.getElementById("switch_contacts")

if (localStorage.getItem('theme') == "true"){
   contacts_theme.href = '../static/dark-theme/dark-contacts.css'
}

else{
    contacts_theme.href = '../static/css/contacts.css'
}