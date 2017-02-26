# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('profile.html')


@app.route('/vivi-1')
def task_1():
    return render_template('task1.html')


@app.route('/vivi-2')
def task_2():
    return render_template('task2.html')

if __name__ == '__main__':
    app.run(debug=True)
