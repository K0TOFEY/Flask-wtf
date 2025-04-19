from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
