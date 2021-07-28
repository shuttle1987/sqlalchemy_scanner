from flask import flask, _app_ctx_stack, jsonify, abort
from sqlalchemy.orm import scoped_session

from . import models
from .database import SessionLocal, engine

app = Flask(__name__)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()


@app.route("/tasks/")
def show_tasks():
    tasks = app.session.query(models.Task).all()
    return jsonify([task.to_dict() for task in tasks])

@app.route("/tasks/<id>")
def get_task(id):
    task = app.session.query(models.Task).filter(Task.id == id).one_or_none()
    if task is None:
        abort(404)
    return jsonify(task.to_dict())