#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template, request, redirect, \
url_for, flash, make_response, session
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'
#...
@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template('index.html')

@app.route('/destroy_session/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'

if __name__=='__main__': 
    app.run(debug=True)