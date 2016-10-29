#!/usr/bin/env python

import os
import sys

from flask import Flask
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
    return DATABASE_FILE


def main():
    return app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())
