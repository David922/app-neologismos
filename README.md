# para instalar todas las herramientas y extensiones de la api
pip install flask flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow-sqlalchemy

# para probar api-neologismos
# linux
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

# Windows
set FLASK_APP=entrypoint:app
set FLASK_ENV=development
set APP_SETTINGS_MODULE=config.default

# desde la carpeta api-neologismos
	# solo la primera vez
	flask db init
	# solo si se hacen cambios en los recursos
	flask db migrate -m "Initial_db"
	flask db upgrade
	# arrancar el servidor (esta configurado en local. peticiones a localhost:5000 con Postman)
	flask run
# Toda la info en:
# https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/#apirest-flaskhttps://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/#apirest-flask

# para instalar todas las herramientas y extensiones de la app-neologismos
# esta lista aun no esta completa
pip install Flask-WTF
pip install email-validator	
pip install flask-login
pip install flask-sqlalchemy
# desde la carpeta api-neologismos	
# para probar app-neologismos
# linux	
export FLASK_APP="run.py"
# Windows
set FLASK_APP=run.py
# desde la carpeta api-neologismos
	# arrancar en local y elegir puerto
	flask run --port 6000
	# arrancar en red
	flask run --host 0.0.0.0
	# para debug
	set "FLASK_ENV=development"
	
# Toda la info en:
# https://j2logo.com/tutorial-flask-espanol/