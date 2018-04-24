import os
from flask import Flask
import cx_Oracle

db_user = 'conocer'
db_password = 'conocer'
dc_connect = ""




app = Flask(__name__) #crea la aplicacion
app.config.from_object(__name__) #lee la configuracion de la aplicacion

@app.route('/')
def index():
    connection = cx_Oracle.connect(db_user, db_password, db_connect)

