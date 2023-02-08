from flask import *
from models.models import *
from models.database import db_session
from datetime import datetime

app=Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")
@app.route("/addbook",methods=["post"])
def adding():
    title=request.form["title"]
    author=request.form["author"]
    conn=Books(title,author)
    db_session.add(conn)
    db_session.commit()
    return 
