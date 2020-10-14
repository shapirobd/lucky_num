from flask import Flask, render_template, jsonify, request
from forms import LuckyForm
import requests
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('index.html')


@app.route('/api/get-lucky-num', methods=['POST'])
def get_lucky_num():
    values = get_values(request.json)
    form = LuckyForm(meta={'csrf': False}, data=values)

    if form.validate():
        num = random.randint(1, 100)
        year = values['year']

        num_fact = get_num_fact(num)
        year_fact = get_year_fact(year)

        return jsonify(num=num_fact, year=year_fact)

    return jsonify(errors=form.errors)


def get_values(data):
    name = data['name']
    email = data['email']
    year = data['year']
    color = data['color']

    return {'name': name, 'email': email, 'year': year, 'color': color}


def get_num_fact(num):
    resp = requests.get(f'http://numbersapi.com/{num}')

    return {
        'fact': resp.text,
        'num': num
    }


def get_year_fact(year):
    resp = requests.get(f'http://numbersapi.com/{year}/year')

    return {
        'fact': resp.text,
        'year': year
    }
