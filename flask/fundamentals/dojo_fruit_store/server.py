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
    print(request.form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    fruits = ["apple", "blackberry", "raspberry", "strawberry"]
    return render_template("fruits.html", fruits=fruits)

#this must be below ALL routes
if __name__=="__main__":   
    app.run(debug=True)    