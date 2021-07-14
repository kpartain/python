#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv install PyMySQL flask ... to make flask server WITH mySQL
#pipenv shell ..... to enter into shell
#python server.py ..... start your server

from flask import Flask, render_template, request, redirect, session
#from file import Class  ... [lowercase file, uppercase Class]
from friend import Friend
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)
            
if __name__ == "__main__":
    app.run(debug=True)