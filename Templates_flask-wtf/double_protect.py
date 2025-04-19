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


@app.route('/answer')
@app.route("/auto_answer")
def auto_answer():
    d = dict()
    d['title'] = 'Анкета'
    d['surname'] = 'Watny'
    d['name'] = 'Mark'
    d['education'] = 'выше среднего'
    d['profession'] = 'штурман марсохода'
    d['sex'] = 'male'
    d['motivation'] = 'Всегда мечтал застрять на Марсе'
    d['ready'] = 'True'
    return render_template('auto_answer.html', data=d, file=url_for('static', filename="css/style.css"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
