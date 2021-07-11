#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.route('/')
def foo():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def post_with_session_redirect():
    print(request.form)
    key_one = request.form['key_one']
    session['username'] = request.form['name']
    return redirect('/show.html')

@app.route('/show')
def after_post_redirect():
    print('Showing the User Info From the Form')
    print(request.form)
    #session data is available to the form without handing it to it in return
    return render_template('show.html')

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)