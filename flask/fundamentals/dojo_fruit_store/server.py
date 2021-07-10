    #pipenv install flask ..... to make pipfile and pipfile.lock
    #pipenv shell ..... to enter into shell
    #python server.py ..... start your server
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    name = request.form.get('first_name') + " " + request.form.get('last_name')
    items = int(request.form.get('strawberry')) + int(request.form.get('raspberry')) + int(request.form.get('apple'))
    print("Charging", name, " for", items, "fruits.")
    purchaseSummary = [
        {'Strawberries': request.form.get('strawberry')},
        {'Raspberries': request.form.get('raspberry')},
        {'Apples': request.form.get('apple')}
    ]
    studentID = request.form.get('student_id')
    if studentID == "":
        studentID = "N/A"
    userData = [
        {'First Name': request.form.get('first_name')},
        {'Last Name': request.form.get('last_name')},
        {'Student ID': studentID}
    ]

    return render_template("checkout.html", purchaseSummary=purchaseSummary, userData = userData)

@app.route('/fruits')         
def fruits():
    fruits = ["apple", "blackberry", "raspberry", "strawberry"]
    return render_template("fruits.html", fruits=fruits)

#this must be below ALL routes
if __name__=="__main__":   
    app.run(debug=True)    