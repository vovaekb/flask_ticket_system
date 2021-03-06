from flask import Flask, _app_ctx_stack, render_template, request, jsonify, Response
from sqlalchemy.orm import scoped_session
from sqlalchemy.exc import SQLAlchemyError
import datetime
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
app.config['JSON_AS_ASCII'] = True 
