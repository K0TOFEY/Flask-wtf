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
    if prof == 'инженер' or prof == 'строитель':
        return render_template('index.html', type_simulator='Инженерные тренажеры')
    else:
        return render_template('index.html', type_simulator='Научные симуляторы')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')