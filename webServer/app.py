from flask import Flask, render_template, Response,request, jsonify
import numpy as np
import time
app = Flask(__name__)
import readData as rd


@app.route("/get_data", methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        # read records from firebase
        # data = rd.readData(page,count)
        count = request.values['count']
        page = request.values['page']
        # data = get_data('page_user', 1)
        data = rd.readData(page, count)
        print(data)
        print(type(data))
        # template_data = {
        #  'keys': data[0],
        #  'values': data[1]
        # }
        return str(data)
    else:
        return render_template('index.html')


def change_threshold():
    # change the goal of volume per inhale in firebase
    pass


@app.route("/", methods=['GET', 'POST'])
def index():
    # return render_template('index.html', **template_data)
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
