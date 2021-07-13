#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server

from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.route('/guess')
def initial_route():
    if "answerDiv" in session:
        session["answerDiv"] = session["answerDiv"]
    else:
        session["answerDiv"] = "<div></div>"
    return render_template('index.html')

@app.route('/guess_post', methods=['POST'])
def post_with_session_redirect():
    print(request.form)
    user_guess = int(request.form['userGuess'])
    computer_answer = random.randint(1, 100)
    if user_guess > computer_answer:
        backgroundColor = "red"
        text = "Too High!"
        buttonVisibity = "none"
    elif user_guess < computer_answer:
        backgroundColor = "red"
        text = "Too Low!"
        buttonVisibity = "none"
    else:
        backgroundColor = "green"
        text = "You guessed it! The number was" + str(computer_answer)
        buttonVisibity = ""

    
    return redirect('/redirect-to-here')


#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)