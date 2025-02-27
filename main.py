from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def base():
    return "<b>Миссия колонизация Марса<b><br/><a href='/index'>Переход к дивизу</a><br/><a href='/promotion'>Переход к рекламе</a><br/><a href='/image_mars'>Переход к картинке Марса</a><br/><a href='/promotion_image'>Переход к картинке Марса с рекламой</a>"


@app.route('/index')
def index():
    return "<b>И на Марсе будут яблони цвести!<b><br/><a href='/'>Переход на главную страницу</a>"


@app.route('/promotion')
def promotion():
    return "<b>Человечество вырастает из детства.<br/>Человечеству мала одна планета.<br/>Мы сделаем обитаемыми " \
           "безжизненные пока планеты.<br/>И начнем с Марса!<br/>Присоединяйся!<b><br/><br/><a href='/'>Переход на главную страницу</a>"


@app.route('/image_mars')
def image_mars():
    return "<title>Картинка Марса</title><h1>Жди нас, Марс!</h1><br/><img src='static/img/mars.png'><br/><p>Вот она какая, красная планета</p><br/><br/><a href='/'>Переход на главную страницу</a>"


@app.route('/promotion_image')
def promotion_image():
    return """<head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head><h1 style='color:red'>Жди нас, Марс!</h1><img src='static/img/mars.png'><br/><div class="alert alert-primary" role="alert" style='background-color: lightgray; color:black'>Человечество вырастает из 
        детства.</div><br/><div class="alert alert-primary" role="alert" style='background-color: lightgreen; color:green'>Человечеству мала одна планета.</div><br/><div class="alert alert-primary" role="alert" style='background-color: lightgray; color:black'>Мы сделаем обитаемыми """ \
           """безжизненные пока планеты.</div><br/><div class="alert alert-primary" role="alert" style='background-color: lightyellow; color:gold'>И начнем с Марса!</div><br/><div class="alert alert-primary" role="alert" style='background-color: pink; color:lightred'>Присоединяйся!</div><br/><br/><a href='/'>Переход на 
           главную страницу</a> """


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert" style='background-color: pink'>
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


@app.route('/choice/<planet>')
def choice(planet):
    return f"""<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" href='static/css/choice.css'>
    <title>Варианты выбора</title>
</head><h1 style="margin-bottom: 10px">Мое предложение: {planet}</h1><h2>Эта планета близка к Земле;</h2>
<div class="alert alert-primary strings" role="alert" style='background-color: lightgray; color:black'>На ней много необходимых ресурсов;</div>
<div class="alert alert-primary strings" role="alert" style='background-color: lightgreen; color:green'>На ней есть вода и атмосфера;</div>
<div class="alert alert-primary strings" role="alert" style='background-color: lightyellow; color:gold'>На ней есть небольшое магнитное поле;</div>
<div class="alert alert-primary strings" role="alert" style='background-color: pink; color:red'>Наконец, она просто красива!</div>
<a href='/'>Переход на главную страницу</a>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" href='static/css/choice.css'>
    <title>Результаты</title>
</head><h1 style="margin-bottom: 10px">Результаты отбора</h1><h2>Претендент на участие в миссии {nickname}:</h2>
<div class="alert alert-primary strings" role="alert" style='background-color: lightgreen; color:green'><h2>Поздравляем! Ваш рейтинг после {level} этапа отбора</h2></div>
<h2>составляет {rating}</h2>
<div class="alert alert-primary strings" role="alert" style='background-color: lightyellow; color:gold'><h2>Желаем удачи!</h2></div>
<a href='/'>Переход на главную страницу</a>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
