from flask import Flask, request
''' 
Ejemplo paramteros, sim parametros y con parametro validado
'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'
    
#ejemplo:http://127.0.0.1:8000/params    

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name='valor por default',num=0):
    return 'El parámetro es : {}{}'.format(name,num)

if __name__ == '__main__':
    app.run(debug=True, port=8000) 


