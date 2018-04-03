from flask import Flask, request
'''
ejemplo de parametros
'''
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'
    
#ejemplo:http://127.0.0.1:8000/params?par1=cris&par2=pedrani    

@app.route('/params')
def params():
    param = request.args.get('par1', 'no contiene parametros')
    param_2 = request.args.get('par2', 'no contiene parametros')
    return 'El parámetro es : {}, {}'.format(param, param_2)

if __name__ == '__main__':
    app.run(debug=True, port=8000) 


