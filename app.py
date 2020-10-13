from flask import Flask, render_template, jsonify, request
import requests
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('index.html')


@app.route('/api/get-lucky-num', methods=['POST'])
def get_lucky_num():

    data = request.json

    name = data['name']
    email = data['email']
    year = data['year']
    color = data['color']

    num = random.randint(1, 100)

    num_fact = get_num_resp(num)
    year_fact = get_year_resp(year)

    return jsonify(num=num_fact, year=year_fact)


def get_num_resp(num):
    num_resp = requests.get(f'http://numbersapi.com/{num}')
    num_fact = {
        'fact': num_resp.text,
        'num': num
    }
    return num_fact


def get_year_resp(year):
    year_resp = requests.get(f'http://numbersapi.com/{year}/year')
    year_fact = {
        'fact': year_resp.text,
        'year': year
    }
    return year_fact
