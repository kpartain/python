from flask_app import app
from flask import render_template,redirect,request,flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def register_or_login():
    if 'user_first_name' in session:
        session['user_first_name'] = session['user_first_name']
    else:
        session['user_first_name'] = ""
    if 'user_id' in session:
        session['user_id'] = session['user_id']
    else:
        session['user_id'] = ""
    #if there is nobody logged in, start a session for registration data so they can correct
    #any errors rather than type everything again 
    if session['user_id'] is "":
        if 'first_name' not in session:
            session['first_name'] = ""
        if 'last_name' not in session:
            session['last_name']
        if 'email' not in session:
            session['email']
    return render_template('register_or_login.html')

@app.route('/success')
def redirect_success():
    if session['user_first_name'] == "":
        return redirect('/')
    else:
        return render_template("success.html")

@app.route('/new-user-post', methods=["GET", "POST"])
def register_new_user():
    #if there are errors, save the current input to session except password
    #this way user can correct mistake rather than retype it
    if User.validate_user(request.form) == False:
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/')
    #OTHERWISE, if it is valid,hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print("PWHASH",pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
        }
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    returnedObject = User.register_and_login(data)
    print("OBJ after PWHASH", returnedObject)
    session['user_first_name'] = returnedObject.first_name
    session['user_id'] = returnedObject['id']
    session['success_message'] = "You've been successfully registered!"
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
        flash("Invalid Email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_first_name'] = user_in_db.first_name
    session['user_id'] = user_in_db.id
    session['success_message'] = "You've been logged in!"
    return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    #clear session
    session.clear()
    session['user_id'] = ""
    session['user_first_name'] = ""
    return redirect('/')

