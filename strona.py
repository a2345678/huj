# -*- coding: utf-8 -*-
from flask import Flask, render_template
from math import sqrt

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/sranierazjeszce')
def sranie():
    return 'sram'


@app.route('/sronda')
def sr():
    return render_template('sr.html', header='Hello', sreader=6, jebac=sqrt(45))



if __name__ == '__main__':
    app.run('0.0.0.0', port=2137, debug=True)

