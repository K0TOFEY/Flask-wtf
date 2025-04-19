from flask import Flask, render_template, url_for, request

app = Flask(__name__)

ans = dict()


@app.route('/')
@app.route('/index')
def index():
    return "Привет Яндекс"


@app.route('/index/<title>')
def with_name(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def profession(prof):
    img_name = 'science.jpg'
    simu_name = 'Научные симуляторы'
    if ('инженер' in prof.lower()) or ('строитель' in prof.lower()):
        img_name = 'eng.jpg'
        simu_name = 'Инженерные тренажеры'
    return render_template('index.html', img=url_for('static', filename=f'img/{img_name}'), type_simulator=simu_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('double_protect.html', file=url_for('static', filename='img/MARS-2-7.png'))


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    global ans
    if request.method == 'GET':
        return f"""<!doctype html>
    <html lang="en">    
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href='{url_for('static', filename='css/style.css')}' />
        <title>Пример формы</title>
      </head>
      <body>
        <h1 class="f">Анкета претендента</h1>
        <h2>на участие в миссии</h2>
        <div>
            <form class="login_form" method="post">
                <div class="input-group mb-3">
                  <input type="surname" class="form-control" placeholder="Введите фамилию" aria-label="Username" aria-describedby="basic-addon1" name="surname">
                    <input type="name" class="form-control" placeholder="Введите имя" aria-label="Username" aria-describedby="basic-addon1" name="name">
                </div>
                <div class="input-group mb-3">
                  <input type="mail" class="form-control" placeholder="Введите адрес почты" aria-label="Username" aria-describedby="basic-addon1" name="mail">
                </div>
                <div>
                     <label class="form-label">Какое у Вас образование?</label>
                    <select class="form-select" aria-label="Default select example" name="school">
                      <option selected>Начальное</option>
                      <option value="2">Среднее</option>
                      <option value="3">Высшее</option>
                    </select>
                </div>
                <div>
                    <label class="form-label">Какие у Вас есть профессии</label>
                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="eng" id="1">
                      <label class="form-check-label" for="1">
                        Инженер-исследователь
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="eng2" id="2">
                      <label class="form-check-label" for="2">
                        Инженер-строитель
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="pilot" id="3">
                      <label class="form-check-label" for="3">
                        Пилот
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="" id="4">
                      <label class="form-check-label" for="4">
                        Метеоролог
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="" id="5">
                      <label class="form-check-label" for="5">
                        Инженер по жизнеобеспечению
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="" id="6">
                      <label class="form-check-label" for="6">
                        Инженер по радиационной защите
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="" id="7">
                      <label class="form-check-label" for="7">
                        Врач
                      </label>
                    </div>

                    <div class="form-check">
                      <input class="form-check-input" name="prof" type="checkbox" value="" id="8">
                      <label class="form-check-label" for="8">
                        Экзобиолог
                      </label>
                    </div>
                </div>

                <div>
                    <label class="form-label">Укажите пол</label>
                    <div class="form-check">
                      <input class="form-check-input" name="sex" type="radio" value="male" name="flexRadioDefault" id="11">
                      <label class="form-check-label" for="11">
                        Мужской
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" name="sex" type="radio" value="female" name="flexRadioDefault" id="22">
                      <label class="form-check-label" for="22">
                        Женский
                      </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="about">Почему Вы хотите принять участие в миссии?</label>
                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                </div>
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>

                <div class="form-group form-check">
                    <input type="checkbox" value="True" class="form-check-input" id="acceptRules" name="accept">
                    <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
      </body>
    </html>"""
    elif request.method == 'POST':
        ans['surname'] = request.form['surname']
        ans['name'] = request.form['name']
        ans['education'] = request.form['school']
        ans['profession'] = request.form.getlist('prof')
        ans['sex'] = request.form['sex']
        ans['motivation'] = request.form['about']
        ans['ready'] = request.form['accept']
        return "ок"


@app.route('/answer')
@app.route("/auto_answer")
def auto_answer():
    global ans
    return render_template('auto_answer.html', data=ans, file=url_for('static', filename="css/style.css") )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
