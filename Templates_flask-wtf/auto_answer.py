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
    if ('инженер' in prof) or ('строитель' in prof):
        return render_template('index.html', img_eng=url_for('static', filename='img/eng.jpg'), type_simulator='Инженерные тренажёры')
    else:
        return render_template('index.html', img_science=url_for('static', filename='img/science.jpg'), type_simulator='Научные симуляторы')


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
    return render_template('auto_answer.html', data=d, file=url_for('static', filename="css/style.css") )


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
