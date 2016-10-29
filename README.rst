*******************
Pasos para instalar
*******************


Instalar virtualenvwrapper
==========================

::

    sudo yum install -y python-virtualenvwrapper || sudo apt-get -y install virtualenvwrapper
    source `which virtualenvwrapper.sh`


Escribir tu requirements.txt
============================

Más información: https://pip.readthedocs.io/en/1.1/requirements.html


Crear tu directorio source
==========================

Por lo general usamos un directorio ``src`` porque (en algún momento) tendremos
un directorio ``tests`` y por lo general no queremos distribuir esos junto con
el código fuente.

En este directorio ponemos un ``__init__.py`` para *simular* un paquete: en
realidad este paquete no es usado mas que por nuestro script de empaquetamiento.

Más información: https://docs.python.org/2/tutorial/modules.html#packages

Dentro de este directorio es donde vamos también a crear nuestro árbol de código
de nuestra aplicación. Vamos a iniciar este árbol con un simple ``__init__.py``
donde vamos a declarar la versión simple de nuestra aplicación.


Crear tu setup.py
=================

El archivo ``setup.py`` es el estándar de empaquetado de python. La documentación
de setuptools está en https://setuptools.readthedocs.io/en/latest/

En el archivo de setup vamos a usar la versión que declaramos en nuestro archivo
``__init__.py`` y también vamos a modificar nuestro ``requirements.txt`` para
tomar ventaja de ``virtualenv`` y ``develop mode``


Crear nuestro virtualenv
========================

Previamente instalamos ``virtualenvwrapper``, vamos a crear un ambiente virtual
donde enjaular nuestro ambiente de desarrollo::

    mkvirtualenv fslask

o si ya lo habias creado antes::

    workon fslask

.. NOTE::
   Estos *helpers* estarán disponibles solamente si seguiste previamente::

       source `which virtualenvwrapper.sh`

   Para asegurarse que esto suceda siempre, agrega esta directive a tu archivo
   ``~/.bashrc``

Una vez creado el ``virtualenv``, hay que instalar nuestro paquete local en
*develop mode*, esto se consigue gracias a todo lo que ya hemos hecho hasta el
momento:

1. *virtuaelnv*
2. ``requirements.txt``
3. ``setup.py``
4. nuestro código

Ejecutemos entonces::

    pip install -r requirements.txt

El término *develop mode* se refiere a que dentro de nuestro *virtualenv* en
lugar de que nuestro código se copie, se crean *soft links*, lo cual permite que
cambios guardados cuando estamos editando sean reflejados sin tener que instalar
de nuevo (con algunas restricciones)


Nuestro primer punto de entrada
===============================

Hasta ahora tenemos todo lo necesario para iniciar, pero aun no hemos empezado.
Comencemos por hacer nuestro *"hello world"* en un nuevo módulo dentro de nuestro
árbol de código, digamos, ``src/fslask/server.py``

Este programa va a ser declarado como un punto de entrada de consola en nuestro
``setup.py`` y de esa manera podremos ejecutar este script directamente


Usar una base de datos
======================

Usaremos paquetes extra: Flask-SQLAlchemy por ahora. Hay que agregarla a nuestro
archivo de requerimientos e instalar de nuevo::

    pip install -r requirements.txt

Una vez instalados hay que configurar nuestra app de Flask, la extensión usa
variables globales para configurarse ``SQLALCHEMY_DATABASE_URI`` que por ahora
va a apuntar a un DB SQLite.

Después hay que crear nuestros objetos que estarán guardados en la base de datos,
usaremos 2 clases muy simples: Preguntas y Respuestas.

Después de esto hay que crear la base de datos, vamos a agregar una nueva ruta
que va a crear la DB
