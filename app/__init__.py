from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy

from config import Config

from .logger import initialize_file_logs, initialize_send_mail_logs

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "login"

mail = Mail(app)

recaptcha = ReCaptcha(app=app)

initialize_file_logs(app)
initialize_send_mail_logs(app)

from . import errors, models, routes  # noqa: E402,F401; isort: stop
