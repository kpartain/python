from flask_app import app
from flask import render_template,redirect,request,flash
#gets session from __init__.py ?? or add back?
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def register_or_login():
    if 'user_object' in session:
        session['user_object'] = session['user_object']
    else:
        session['user_object'] = ""
    return render_template('register_or_login.html')

@app.route('/success')
def redirect_success():
    render_response = ""
    #if session['user_object'] is empty, 
        #render "register_or_success.html"
    #otherwise, if session has a user, 
        #render "success.html"
    return render_template(render_response)

@app.route('/new-user-post', methods=["GET", "POST"])
def register_new_user():
    #see if user email already exists in DB - account for capitalization
    lower_case_email = request.form["email"].lower()
    email_data = { 
        "email" : lower_case_email
        }
    user_in_db = User.get_by_email(email_data)
    #if user in DB, return a message asking them to log in
    if user_in_db:
        flash("User found with this email - please log in")
    elif not user_in_db: 
    #validate fields
        #if not valid, refresh. Model handles flashes.
        if not User.validate_user(request.form):
            return redirect('/')
        #OTHERWISE, if it is valid,
        #hash the password
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        # put the pw_hash into the data dictionary
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password" : pw_hash
        }
            #save the user
            #return the user saved
            #save this as session['user_object']
            #store session["message"] "You've been successfully registered!" for page
    return redirect('/success')

@app.route('/login-existing-user-post', methods=["POST"])
def login_existing_user():
    lower_case_email = request.form["email"].lower()
    email_data = { 
        "email" : lower_case_email
        }
    user_in_db = User.get_by_email(email_data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    #clear session
    return redirect('/')