# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(debug=True)