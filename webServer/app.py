from flask import Flask, render_template, Response,request, jsonify
import numpy as np
import time
import readData as rd
import json
app = Flask(__name__)


@app.route("/get_sum", methods=['GET', 'POST'])
def get_sum():
    if request.method == 'POST':
        page = request.values['page']
        sum_num = rd.getSum(page)
        return json.dumps(sum_num)
    else:
        return render_template('index.html')


@app.route("/get_user_page", methods=['GET', 'POST'])
def get_user_page():
    if request.method == 'POST':
        page = request.values['page']
        content = rd.readPage(page)
        return content
    else:
        return render_template('index.html')


@app.route("/get_data", methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        # read records from firebase
        # data = rd.readData(page,count)
        count = request.values['count']
        page = request.values['page']
        # data = get_data('page_user', 1)
        data = rd.readData(page, count)
        return data
    else:
        return render_template('index.html')

def change_threshold():
    # change the goal of volume per inhale in firebase
    pass


@app.route("/", methods=['GET', 'POST'])
def index():
    # return render_template('index.html', **template_data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
