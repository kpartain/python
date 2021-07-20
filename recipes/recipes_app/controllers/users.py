from recipes_app import app
from flask import render_template,redirect,request,flash, session
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe

@app.route('/')
def register_or_login():
    #session to imitate use state for registration form values
    if 'first_name' not in session:
        session['first_name'] = ""
    if 'last_name' not in session:
        session['last_name'] = ""
    if 'email' not in session:
        session['email'] = "request.form['email']"
    return render_template('registration.html')

@app.route('/success')
def redirect_success():
    #if someone manually navigated here and isn't actually logged in
    #note we use 'user_first_name' not first_name from UseState from registration
    if session['user_first_name'] == "":
        return redirect('/')
    else:
        all_recipes = Recipe.find_all()
        return render_template("success.html")

@app.route('/new-user-post', methods=["GET", "POST"])
def register_new_user():
    #update the "use state" registration form values
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    #validate fields, add to db, and log in - will return false or an object
    result = User.register_and_login(request.form)
    if result == False:
                return redirect('/')
    else: 
        session['first_name'] = "" #reset the "UseState"
        session['last_name'] = "" #reset the "UseState"
        session['email'] = "" #reset the "UseState"
        session['user_first_name'] = result.first_name
        session['user_id'] = result.id
        return redirect('/success')

@app.route('/login-existing-user-post', methods=["POST"])
def login_existing_user():
    #validate fields and log in - will return false or an object 
    #I am not doing a UseState here because it may imply the only error was in the PW
    result = User.validate_login(request.form)
    if result == False:
       return redirect('/')
    else : 
        session['user_first_name'] = result.first_name
        session['user_id'] = result.id
        return redirect('/success')

@app.route('/logout-user')
def log_user_out():
    session.clear()
    return redirect('/')