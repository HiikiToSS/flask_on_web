var isShow = true

function show_reg(){
  var del_log = document.getElementById('cont_for_log')
  del_log.classList.remove('animation_for_log')
  var log_button = document.getElementById('cont_for_reg')
  log_button.classList.toggle('animation_for_reg')
}

function show_log(){
  var del_reg = document.getElementById('cont_for_reg')
  del_reg.classList.remove('animation_for_reg')
  var reg_button = document.getElementById('cont_for_log')
  reg_button.classList.toggle('animation_for_log')
}