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