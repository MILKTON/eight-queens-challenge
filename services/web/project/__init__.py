from flask import Flask, jsonify, flash,render_template
from .reinas import coloca_reinas
from .models import soluciones, init_db
from sqlalchemy import update
from .db import Session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
init_db()

# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = \
    '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
@app.route("/")
def hello_world():
  flash('error message', 'error')
  # query a la tabla soluciones 
  # donde reinas = 4
  # selet from soluciones where reinas = 4
  # if existe imprimo
  # else calculamos e insertamos
  solucion = coloca_reinas(4)
  print(solucion)
  solus = Session.query(soluciones).filter_by(reinas=4).first()
  context = {
      'solucion': str(solucion),
      'solus' : solucion
  }
  print(solus.soluciones)
  #solus = Session.query(soluciones).filter_by(reinas=4).first()
  #print(solus.soluciones)

  #ins = soluciones(4,solucion) #creacion de objeto sin guardar en variable
  #ins.insertar_registro()

  #ins = soluciones(4,solucion)
  #Session.add(ins)
  #Session.commit()
  #Session.commit() #para hacer commit al final
  return render_template('base.html', **context)


@app.route('/resuelve/<int:n>', methods=['GET'])
def resuelve(n):
    solucion = coloca_reinas(n)
    context = {
      'solus' : solucion
    }
    return render_template('base.html', **context)


