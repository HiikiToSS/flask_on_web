let langs_theme = document.getElementById("switch_langs")

let c_img = document.getElementById('c_')
let java_img  = document.getElementById('java')
let js_img = document.getElementById('js')
let kotlin_img = document.getElementById('kotlin')
let python_img = document.getElementById('python')
let swift_img = document.getElementById('swift')


if (localStorage.getItem('theme') == "true"){
    if (c_img){c_img.src = '../../static/img/hi/_c++.png'}
    if (java_img){java_img.src = '../../static/img/hi/_java.png'}
    if (js_img){js_img.src = '../../static/img/hi/_js.png'}
    if (kotlin_img){kotlin_img.src = '../../static/img/hi/_kotlin.png'}
    if (python_img){python_img.src = '../../static/img/hi/_python.png'}
    if (swift_img){swift_img.src = '../../static/img/hi/_swift.png'}

    langs_theme.href = '../../static/dark-theme/dark-langs.css'
}

else{
    if (c_img){c_img.src = '../../static/img/hi/l_c++.png'}
    if (java_img){java_img.src = '../../static/img/hi/l_java.png'}
    if (js_img){js_img.src = '../../static/img/hi/l_js.png'}
    if (kotlin_img){kotlin_img.src = '../../static/img/hi/l_kotlin.png'}
    if (python_img){python_img.src = '../../static/img/hi/l_python.png'}
    if (swift_img){swift_img.src = '../../static/img/hi/l_swift.png'}
    
    langs_theme.href = '../../static/langs.css'
}

/*сделай изменение фото по айдишникам из массива (цикл по колву элементов, давно же такого не было, ностальгия по питошке))*/