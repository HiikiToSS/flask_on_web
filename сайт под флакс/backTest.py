from flask import Flask, render_template, request, flash, redirect, session, url_for, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LmaoWhatAPassword'

menu = [
    {'name' : 'О сайте', 'url' : 'about'},
    {'name' : 'Обратная связь', 'url' : 'contact'},
    {'name' : 'Информация', 'url' : 'info'}
    ]

nav_menu = [
    {'name' : 'О сайте', 'url' : 'about'},
    {'name' : 'Языки программирования', 'url' : 'language'},
    {'name' : 'Контакты', 'url' : 'contact'},
    {'name' : 'На главную', 'url' : 'main'}
]

@app.route('/')
@app.route('/main')
def index():
    return render_template('__index.html', title='Главная', navi_menu=nav_menu)

@app.route('/language')
def language():
    return render_template('language.html', title='Языки программирования', navi_menu=nav_menu)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты', navi_menu=nav_menu)

@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')

@app.errorhandler(404)
def NotFound(error):
    return render_template('page404.html', title='Такой страницы нет', navi_menu=nav_menu), 404

if __name__ == '__main__':
    app.run(debug=True)