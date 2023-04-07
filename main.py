from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json


class LoginForm(FlaskForm):
    id_as = StringField('id астронавта', validators=[DataRequired()])
    as_pass = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('id капитана', validators=[DataRequired()])
    cap_pass = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<name>')
@app.route('/index/<name>')
def name_page(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def train(prof):
    dct = {"строитель": 1, "инженер": 2}
    fl = 3
    if prof in dct:
        fl = dct[prof]
    return render_template('train.html', fl=fl)


@app.route('/list_prof/<lst>')
def lst_proof(lst):
    dct = {"ul": 2, "ol": 1}
    fl = 3
    if lst in dct:
        fl = dct[lst]
    return render_template('lst_prof.html', fl=fl)


@app.route('/answer')
@app.route('/auto_answer')
def ans():
    title = "Письмо"
    surname = "Watny"
    name = "Mark"
    education = "выше среднего"
    profession = "штурман марсохода"
    sex = "male"
    motivation = "Всегда мечтал застрять на Марсе!"
    ready = "True"
    quest = {"title": title, "Фамилия:": surname, "Имя:": name, "Образование:": education,
         "Профессия:": profession, "Пол:": sex, "Мотивация:": motivation, "Готовы остаться на Марсе?": ready}
    return render_template('auto_answer.html', dct=quest)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


@app.route('/distribution')
def dist():
    lst = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', lst=lst)


@app.route('/table/<gender>/<age>')
def table(gender, age):
    female_ad = "/static/images/female_ad.png"
    female_kid = "/static/images/female_kid.png"
    male_kid = "/static/images/male_ad.png"
    male_ad = "/static/images/male_kid.jpg"
    ad = "/static/images/adult.jpg"
    kid = "/static/images/kid.jpg"
    age_tmp = kid
    color_tmp = male_kid
    if gender == "female":
        color_tmp = female_kid
    if int(age) >= 21:
        age_tmp = ad
        if gender == "female":
            color_tmp = female_ad
        else:
            color_tmp = male_ad
    print(color_tmp)
    return render_template('table.html', color_tmp=color_tmp, age_tmp=age_tmp)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')