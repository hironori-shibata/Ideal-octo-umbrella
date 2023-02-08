from flask import *

app=Flask(__name__)

def check(boo):
    if boo == None:
        return False
    

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/addbook",methods=["post"])
def adding():
    return render_template("home.html")
    