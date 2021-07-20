from recipe_app import app
from flask import render_template,redirect,request,flash, session
from recipe_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def register_or_login():
    if 'user_first_name' in session:
        session['user_first_name'] = session['user_first_name']
    else:
        session['user_first_name'] = ""
    return render_template('register_or_login.html')

@app.route('/success')
def redirect_success():
    if session['user_first_name'] == "":
        return redirect('/')
    else:
        return render_template("success.html")

@app.route('/new-user-post', methods=["GET", "POST"])
def register_new_user():
    if User.validate_registration(request.form) == False:
                return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
        }
    returnedObject = User.register_and_login(data)
    session['user_first_name'] = returnedObject.first_name
    session['success_message'] = "You've been successfully registered!"
    return redirect('/success')

@app.route('/login-existing-user-post', methods=["POST"])
def login_existing_user():
    request.form['login_password'] = 
    if User.validate_login(request.form) == False:
       return redirect('/')
    data = {
        'email' : request.form['email']
    }
    logged_in_user = User.get_by_email(data)
    # if the passwords matched, we set the user_id into session
    session['user_first_name'] = logged_in_user.first_name
    session['user_id'] = logged_in_user.id
    session['success_message'] = "You've been logged in!"
    return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    #clear session
    session.clear()
    return redirect('/')