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

