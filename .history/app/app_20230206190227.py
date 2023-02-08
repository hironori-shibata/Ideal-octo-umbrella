from flask import *

app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html")
@app.route("/addbook",methods="post")
def adding():
    return render_template("home.html")
    