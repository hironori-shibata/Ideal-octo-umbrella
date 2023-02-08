from flask import *

app=Flask(__name__)

def check

@app.route("/")
def hoem():
    return render_template("home.html")
@app.route("/addbook",methods=["post"])
def adding():
    return render_template("home.html")
    