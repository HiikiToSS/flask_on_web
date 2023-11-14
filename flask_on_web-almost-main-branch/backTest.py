from flask import Flask, render_template, request, flash, redirect, session, url_for, abort
from pymongo import MongoClient
import pymongo
import pprint
import time

# import dns.resolver
# dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
# dns.resolver.default_resolver.nameservers=['8.8.8.8']


CONNECTION_STRING = "mongodb+srv://hikki_bd:Ares_0377@cluster0.yv7ke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client['NOT_fucking_db_for_test'] #DATA_BASE_for_prog_wiki_ru
collection = db["Data-for-language-html"] # создаём коллекцию


app = Flask( __name__,
    template_folder='templates',
    static_folder='static'   
)

lang_desc_add = [
    {'lang_name' : 'JavaScript', 'link' : 'JavaScript', 
        'title' : 'JavaScript - как живая вода для сайтов', 'hello' : 'Hello World на JavaScript', 
        'photoLight' : 'l_js.png', 'photoDark' : '_js.png',
        'desc' : '("JS" для краткости) - это полноценный динамический язык программирования, который применяется к HTML документу, и может обеспечить динамическую интерактивность на веб-сайтах.'},
    
    {'lang_name' : 'Python', 'link' : 'Python', 
        'title' : 'Python - простой и понятный даже чайнику', 'hello' : 'Hello World на Python', 
        'photoLight' : 'l_python.png', 'photoDark' : '_python.png',
        'desc' : ' – универсальный язык рпограммирования высокого уровня, его преимущества: высокая производительность и хорошо читаемый код. Синтаксис питона максимально облегчен, что позволяет выучить его за сравнительно короткое время.'},
    
    {'lang_name' : 'C++', 'link' : 'C++', 
        'title' : 'C++ - о его сложности слагают легенды...', 'hello' : 'Hello World на C++', 
        'photoLight' : 'l_c++.png', 'photoDark' : '_c++.png',
        'desc' : ' - широко использующийся язык программирования для разработки ПО, высокопроизводительных серверов и развлекательных приложений, является одним из самых популярных языков прогарммирования.'},
    
    {'lang_name' : 'Swift', 'link' : 'Swift', 
        'title' : 'Swift - что-то на богатом', 'hello' : 'Hello World на Swift', 
        'photoLght' : 'l_swift.png', 'photoDark' : '_swift.png',
        'desc' : ' - язык программирования от Apple с открытым исходным кодом. Предназначен для разработки приложений для iOS и macOS, реже используется в других проектах. Он появился всего в 2014 году как альтернатива Objective-C.'},
    
    {'lang_name' : 'Kotlin', 'link' : 'Kotlin', 
        'title' : 'Kotlin - для android приложений', 'hello' : 'Hello World на Kotlin', 
        'photoLight' : 'l_kotlin.png', 'photoDark' : '_kotlin.png',
        'desc' : ' - язык программирования, созданный в компании JetBrains. Его разработали в 2011 году на замену Java, который в компании считали слишком многословным.. Новый язык получился на 40% компактнее предшественника.'},
    
    {'lang_name' : 'Java', 'link' : 'Java', 
        'title' : 'Java - некоторые называют жабой', 'hello' : 'Hello World на Java', 
        'photoLight' : 'l_java.png', 'photoDark' : '_java.png',
        'desc' : ' - Java – это быстрый, безопасный и надежный язык программирования для всего: от мобильных приложений и корпоративного ПО до приложений для работы с большими данными и серверных технологий.'},
]

# collection.insert_many(lang_desc_add)

# for el in langs_description:
#     print(el)

app.config['SECRET_KEY'] = 'LmaoWhatAPassword'

nav_menu = [
    {'name' : 'На главную', 'url' : 'main'},
    {'name' : 'Языки программирования', 'url' : 'language'},
    {'name' : 'О сайте', 'url' : 'about'},
    {'name' : 'Контакты', 'url' : 'contact'}
]

@app.route('/')
@app.route('/main')
def index():
    return render_template('mainPage.html', title='Главная', navi_menu=nav_menu)

@app.route('/language')
def language():
    langs_description = collection.find() # Getting info about langs from db, but it takes too long. I have to fix it
    return render_template('language.html', title='Языки программирования', navi_menu=nav_menu, language_description=lang_desc_add)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты', navi_menu=nav_menu, tg='@Kafiynik', vk='ares_0377', gmail='tephton1200@gmail.com')

@app.route('/about')
def about():
    return render_template('about.html', title='О сайте', navi_menu=nav_menu)

@app.route('/test')
def test():
    return render_template('z_test.html', title='Тестовая страница')

@app.errorhandler(404)
def NotFound(error):
    return render_template('page404.html', title='Такой страницы нет', navi_menu=nav_menu), 404

@app.route("/<name>")
def allLLpage(name):
   for el in lang_desc_add:
     if el["lang_name"] == name:
        return render_template("AllPage.html", langInfo = el, navi_menu=nav_menu)

if __name__ == '__main__':
    app.run(debug=True)