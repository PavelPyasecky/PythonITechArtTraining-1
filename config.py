import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # SQLalchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET KEYS
    SECRET_KEY = os.getenv("SECRET_KEY")
    CSRF_ENABLED = os.getenv("CSRF_ENABLED")

    # Gravatar API url
    GRAVATAR_URL = "https://www.gravatar.com/avatar/"

    # Recaptcha Google Keys
    RECAPTCHA_ENABLED = False
    RECAPTCHA_THEME = "dark"  # 'light' - default
    RECAPTCHA_TYPE = "image"  # 'image' - default
    RECAPTCHA_SIZE = "normal"  # 'normal' - default
    RECAPTCHA_SITE_KEY = "6LfPUPobAAAAAPvB8GjZT3QuHtzwYOJ1UyBVbQhH"
    RECAPTCHA_SECRET_KEY = "6LfPUPobAAAAADWFq3kACZJdHe-ZNLmWluUnKKta"
