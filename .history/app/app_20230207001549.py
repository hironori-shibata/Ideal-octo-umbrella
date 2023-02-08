from flask import *
from models.models import *
from models.database import db_session
from datetime import datetime

app=Flask(__name__)
app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('message')
app.logger.error('error')
app.logger.critical('critical')

@app.route("/")
def home():

    return render_template("home.html")
@app.route("/addbook",methods=["post"])
def adding():

    title=request.form["title"]
    author=request.form["author"]
    return [title,author]
    conn=Books(title,author,datetime.now())
    db_session.add(conn)
    db_session.commit()
    return redirect("/")
@app.route("/addshelf",methods=["post"])
def shelf():
    name=request.form["name"]
    conn=Shelfs(name)
    db_session.add(conn)
    db_session.commit()
    return redirect("/")

