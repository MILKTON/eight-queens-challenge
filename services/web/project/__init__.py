from flask import Flask, jsonify
from .reinas import coloca_reinas
from .models import soluciones, init_db
from sqlalchemy import update
from .db import Session

app = Flask(__name__)
init_db()

@app.route("/")
def hello_world():
  # query a la tabla soluciones 
  # donde reinas = 4
  # selet from soluciones where reinas = 4
  # if existe imprimo
  # else calculamos e insertamos
  solucion = coloca_reinas(4)
  print(solucion)

  #solus = Session.query(soluciones).filter_by(reinas=4).first()
  #print(solus.soluciones)

  #ins = soluciones(4,solucion) #creacion de objeto sin guardar en variable
  #ins.insertar_registro()

  #ins = soluciones(4,solucion)
  #Session.add(ins)
  #Session.commit()
  Session.commit() #para hacer commit al final
  return jsonify(solucion)