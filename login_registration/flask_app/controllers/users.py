from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

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

@app.route('/new-user-post', methods=["POST"])
def register_new_user():
    #REGEX: 
        #trim fields to ensure first_name, last_name and password are not empty strings
            #fn, ln 2+ chars, password 8+ chars
        #use pattern matching on email
            #if not EMAIL_REGEX.match(user['email']): 
                #flash("Invalid email address!")
                #is_valid = False
    #see if user email already exists in DB - account for capitalization
        #if user in DB, return a message asking them to log in
    #otherwise if it is a new user,
        #save the user
        #return the user saved
        #save this as session['user_object']
        #store session["message"] "You've been successfully registered!" for page
    return redirect('/success')

@app.route('/login-existing-user-post', methods=["POST"])
def login_existing_user():
    #is email in the database? account for capitalization
        #if yes, now validate password
        #if no, return error "user does not exist - register?"
    #save this as session['user_object]
    return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    #clear session
    return redirect('/')