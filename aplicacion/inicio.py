from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'Base de conocimiento'
    return render_template('index.html', titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
