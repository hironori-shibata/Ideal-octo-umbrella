from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html")
@app.route("/addbook")
def adding():
    