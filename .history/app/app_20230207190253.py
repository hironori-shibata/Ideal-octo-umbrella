from flask import *
from models.models import Books
from models.database import db_session
from datetime import datetime
import time
app=Flask(__name__)
def ocr():
    return True

@app.route("/")
def home():
    shelfs=Shelfs.query.all()


    return render_template("home.html",shelfs=shelfs)
@app.route("/addbook",methods=["post"])
def adding():

    title=request.form["title"]
    author=request.form["author"]
   
    conn=Books(title,author,datetime.now())
    db_session.add(conn)
    db_session.commit()
    db_session.close()
    return redirect("/")
@app.route("/addshelf",methods=["post"])
def shelf():
    name=request.form["name"]
    conn=Shelfs(name)
    db_session.add(conn)
    db_session.commit()
    db_session.close()
    return redirect("/")
@app.route("/ocr")
def recognize():
    picture=request.files["picture"]
    shelf_id=request.form["shelf_id"]
    rename=time.time()
    picture.save(os.path.join("/images",rename))
    
    ocr(picture,shelf_id)

if __name__ == '__main__':
    app.run(debug=True)

