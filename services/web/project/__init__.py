from flask import Flask, jsonify, flash,render_template
from .reinas import coloca_reinas
from .models import soluciones, init_db
from sqlalchemy import update
from .db import Session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
init_db()

# in production app, these should be configured through Flask-Appconfig, used for Boostrap
# https://programtalk.com/vs2/python/6129/inquire/app.py/
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

@app.route("/")
def index():
    solucion = coloca_reinas(8)
    context = {
        'solus' : solucion,
        'total' : len(solucion),
        'n' : 8
    }
    return render_template('base.html', **context)


@app.route('/resuelve/<int:n>', methods=['GET'])
def resuelve(n):
    solucion = coloca_reinas(n)
    total = len(solucion)
    context = {
      'solus' : solucion,
      'total' : total,
      'n' : n
    }
    return render_template('base.html', **context)

@app.route('/dbinsert/<int:n>', methods=['GET'])
def dbinsert(n):
    solucion = coloca_reinas(n)
    total = len(solucion)

    for x in range(n+1):
        if not(Session.query(soluciones).filter_by(reinas=x).first()):
            ins = soluciones(x,solucion) #creacion de objeto sin guardar en variable
            ins.insertar_registro()
            Session.add(ins)
            Session.commit()

    context = {
      'solus' : solucion,
      'total' : total,
      'n' : n
    }
    return render_template('db.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


# Referencias
#    https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
#    https://levelup.gitconnected.com/dockerizing-a-flask-application-with-a-postgres-database-b5e5bfc24848
#    https://medium.com/@hmajid2301/implementing-sqlalchemy-with-docker-cb223a8296de