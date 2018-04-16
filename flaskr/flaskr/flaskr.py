# all te imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__) # crea la aplicacion
app.config.from_object(__name__) #lee la configuracion de este archivo

#carga la configuracion default y sobre escribe la configuracion desde na variable de entorno
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='depelopment key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASK_SETTINGS',silent=True)

def connect_db():
    """ Conexion a la base especificada"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Inicializa las base de datos"""
    init_db()
    print('Inicialiazando la base de datos')

def get_db():
    """Abre una nueva conexion a la base de datos si no está establecida
     en el contexto e la apicacion actualentorno
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Cierra la base de datos cuando el fin es solicitado """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?,?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('La nueva entrada ha sido posteada satisfactoriamente')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Usuario invalido'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Contraseña invalida'
        else:
            session['logged_in'] = True
            flash('Se ha logueado')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Se deslogueo')
    return redirect(url_for('show_entries'))
