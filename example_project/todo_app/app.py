from flask import flask, _app_ctx_stack
from sqlalchemy.orm import scoped_session

from . import models
from .database import SessionLocal, engine

app = Flask(__name__)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()