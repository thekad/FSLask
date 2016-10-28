#!/usr/bin/env python


from flask import Flask
import sys
# importar variables desde el __init__.py local

from . import __name__, __version__, __desc__


app = Flask('fslask')


# route() por default usa el metodo GET
@app.route('/')
def root():
    return '{0} v{1}: "{2}"'.format(__name__, __version__, __desc__)


def main():
    return app.run(debug=True)


if __name__ == '__main__':
    sys.exit(main())
