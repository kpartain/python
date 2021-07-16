from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def kara_is_lazy():
    redirect('/users')

@app.route('/users')
def showUsers():
    usersFromDB = User.get_all_users()
    return render_template('read.html', allUsers = usersFromDB)

@app.route('/users/new')
def showForm():
    return render_template('create.html')

@app.route('/formsubmission', methods=["POST"])
def saveDataFromFormSendToDB():
    data = {
        "first_name" : request.form['first_name'],
        "last_name": request.form['last_name'],
        "email" : request.form['email']
    }
    User.add_new_user(data)
    return redirect("/users")

@app.route('/users/<user_id>')
def show_single_user(user_id):
    find_id = int(user_id)
    data = {
        "id" : find_id
    }
    userFound = User.get_single_user(data)
    return render_template('show.html', singleUser = userFound)

@app.route('/users/<user_id>/edit')
def edit_single_user(user_id):
    find_id = int(user_id)
    data = {
        "id" : find_id
    }
    userFound = User.get_single_user(data)
    return render_template('edit.html', singleUser = userFound)

@app.route('/editsubmission', methods=["POST"])
def save_data_from_form_update_db():
    redirect_to_here = "users/"+request.form['id']
    data = {
        "id": request.form['id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.update_single_user(data)
    return redirect(redirect_to_here)