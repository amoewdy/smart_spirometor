from flask import Flask, render_template, Response,request, jsonify
import numpy as np
import time
app = Flask(__name__)


def get_data():
    # read records from firebase
    pass


def change_threshold():
    # change the goal of volume per inhale in firebase
    pass


@app.route("/",methods=['GET', 'POST'])
def index():
    time_now = time.asctime(time.localtime(time.time()))
    print(time)
    readings = get_data()
    goal = 4500
    achieved = 5/7
    templateData = {
        'time': time_now,
        'goal': goal,
        'achieved': achieved,
    }
    return render_template('index.html', **templateData)


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
