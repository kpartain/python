#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.route('/')
def initial_route():
    if 'yourGold' in session:
        session["yourGold"] = session["yourGold"]
    else:
        session["yourGold"] = 0
    print(session["myString"])
    #this should have access to yourGold from Session
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def post_with_session_redirect():
    #determine how much money to give or take away
    value = 0
    session["myString"] = ""
    if request.form['building'] == 'farm':
        value = random.randint(10, 20)
        session["yourGold"] += value
        session["myString"] = "Earned"
        print(session["myString"])
    elif request.form['building'] == 'cave':
        value = random.randint(5,10)
        session["yourGold"] += value
    elif request.form['building'] == 'house':
        value = random.randint(2,5)
        session["yourGold"] += value
    elif request.form['building'] == 'casino':
        value = random.randint(-50,50)
        session["yourGold"] += value
    #redirect to localhost:5000/
    if value > 0:
        session["myString"] = "Earned " + str(value) + " golds from the " + request.form['building']
        print(session["myString"])
    elif value < 0:
        session["myString"] = "Entered a " + request.form['building'] + " and lost " + str(abs(value)) + " golds... Ouch!"
    else:
        session["myString"] =  "Entered a " + request.form['building'] + " and didn't win or lose. Weird."
    return redirect('/')

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)