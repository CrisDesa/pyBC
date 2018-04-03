from flask import Flask
from flask import render_template
'''
ejemplo de arcivos estaicos css, js, img
'''
app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Aprendiendo Flask'
    return render_template('index3.html', titulo=titulo)
    

if __name__ == '__main__':
    app.run(debug=True, port=8000) 


