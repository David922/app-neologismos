# para instalar todas las herramientas
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
	
