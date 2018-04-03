from flask import Flask
from flask import render_template
'''
ejemplo de herencia de template
'''
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Emi'
    return render_template('index2.html', name=name)
    
@app.route('/cliente')
def cliente():
    lista_nombres = ['Em', 'Teo' , 'Otoño']
    return render_template('clientes.html', lista=lista_nombres)


if __name__ == '__main__':
    app.run(debug=True, port=8000) 


