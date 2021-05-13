export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

set FLASK_APP=entrypoint:app
set FLASK_ENV=development
set APP_SETTINGS_MODULE=config.default

flask db init
flask db migrate -m "Initial_db"
flask db upgrade

flask run