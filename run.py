from app import app, db
from app.models import Post, User


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run(debug=app.config["FLASK_DEBUG"])
