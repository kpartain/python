#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.route('/')
def foo():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def post_with_session_redirect():
    print(request.form)
    session['your_name'] = request.form.get('your_name')
    session['dojo_location'] = request.form.get('dojo_location')
    session['favorite_language'] = request.form.get('favorite_language')
    session['comment_optional'] = request.form.get('comment_optional')
    #access all values from checkbox
    session['pets'] = request.form.getlist('pets')
    return redirect('/result')

@app.route('/result')
def after_post_redirect():
    print('Showing the User Info From the Form')
    print(session['pets'])
    #session data is available to the form without handing it to it in return
    return render_template('result.html')

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)