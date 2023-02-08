from flask import *
from models.models import Books
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
   
    conn=Books(title,author,datetime.now())
    #db_session.add(conn)
    #db_session.commit()
    return redirect("/")
@app.route("/addshelf",methods=["post"])
def shelf():
    name=request.form["name"]
    conn=Shelfs(name)
    db_session.add(conn)
    db_session.commit()
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)

