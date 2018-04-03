#-*- coding: utf-8 -*-
'''
codigo ejemplo llamada a templates
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
@app.route('/user/<name>')
def user( name='usuario'):
    #name='Cris'
    age=48
    lista=[1,2,3,4]
    return render_template('user.html', name=name, age=age, lista=lista)

if __name__ == '__main__':
    app.run(debug=True, port=8000) 


