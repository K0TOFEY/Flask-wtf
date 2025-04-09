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
        return render_template('index.html', img_eng=url_for('static', filename='img/eng.jpg'), type_simulator='Инженерные тренажёры')
    else:
        return render_template('index.html', img_science=url_for('static', filename='img/science.jpg'), type_simulator='Научные симуляторы')


@app.route('/list_prof/<list_type>')
def table_time(list_type):
    if list_type == "ol":
        return render_template('table_ol.html')
    elif list_type == "ul":
        return render_template('table_ul.html')
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')