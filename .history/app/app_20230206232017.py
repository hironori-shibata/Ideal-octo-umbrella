from flask import *
from models.models import *

app=Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")
@app.route("/addbook",methods=["post"])
def adding():
    title=request.form["title"]
    author=request.form["author"]
    return render_template("home.html")
"""@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()"""  