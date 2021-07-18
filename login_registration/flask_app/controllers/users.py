from flask_app import app
from flask import render_template,redirect,request,flash, session
#gets session from __init__.py ?? or add back?
from flask_app.models.user import User
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
    pw1 = request.form['password']
    print("PW1", pw1)
    pw2 = request.form['confirm_password']
    print("PW2",pw2)
    if pw1 != pw2:
        flash("Passwords must match!")
        return redirect('/')
    #see if user email already exists in DB - account for capitalization
    lower_case_email = request.form["email"].lower()
    print("LOWEREMAIL", lower_case_email)
    email_data = { 
        "email" : lower_case_email
        }
    user_in_db = User.get_by_email(email_data)
    print("UserinDB", user_in_db)
        #if user in DB, return a message asking them to log in
    if user_in_db is True :
            flash("This email is already registered to an account - please log in.")
            return redirect('/')
    if not User.validate_user(request.form):
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
    returnedObject = User.register_and_login(data)
    print("OBJ after PWHASH", returnedObject)
    session['user_first_name'] = returnedObject.first_name
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
    return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    #clear session
    session.clear()
    session['user'] = ""
    return redirect('/')