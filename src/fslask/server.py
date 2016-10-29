#!/usr/bin/env python

import os
import sys

from flask import Flask
from flask import request
from flask import Response
from flask import url_for
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

# importar variables desde el __init__.py local
from . import __name__, __version__, __desc__

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask('fslask')

DATABASE_FILE = os.path.abspath(os.path.join(basedir, '..', '..', 'fslask.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(DATABASE_FILE)

db = SQLAlchemy(app)


class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    respuestas = db.relationship('Respuesta')

    def __repr__(self):
        return '<Pregunta: "{0}?">'.format(self.texto)


class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'))

    def __repr__(self):
        return '<Respuesta: "{0}">'.format(self.texto)


# route() por default usa el metodo GET
@app.route('/')
def root():
    app.logger.info('App config: {0}'.format(app.config))
    return '{0} v{1}: "{2}"'.format(__name__, __version__, __desc__)


@app.route('/crear')
def crear_db():

    if not os.path.exists(DATABASE_FILE):
        db.create_all()
        msg = 'creado'
    else:
        msg = 'ya existe'
    return 'Archivo de DB {0} {1}'.format(DATABASE_FILE, msg)


@app.route('/preguntas', methods=['GET'])
def listar_preguntas():
    ps = []
    for p in Pregunta.query.all():
        ps.append({
            'id': p.id,
            'texto': p.texto,
            'timestamp': p.timestamp,
        })
    return jsonify(ps)


@app.route('/preguntas/<pid>')
def mostrar_pregunta(pid):
    p = Pregunta.query.get(pid)
    r = {}
    if p:
        r['id'] = p.id
        r['texto'] = p.texto
        r['timestamp'] = p.timestamp
    return jsonify(r)


@app.route('/preguntas', methods=['POST'])
def crear_pregunta():
    texto = request.form['texto']
    p = Pregunta(texto=texto)
    db.session.add(p)
    db.session.commit()
    resp = Response(status=201)
    resp.headers['Location'] = url_for('mostrar_pregunta', pid=p.id)
    return resp


def main():
    return app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())
