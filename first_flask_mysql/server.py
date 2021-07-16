from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
#what do you want the URL to be?
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    #what HTML file should render? 
    # does the HTML need to access any variable from here?
    return render_template("index.html", all_friends = friends)
# relevant code snippet from server.py
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)