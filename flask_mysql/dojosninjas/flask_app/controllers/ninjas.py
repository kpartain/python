from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def show_form():
    dojos = Dojo.select_all()
    return render_template('new-ninja.html', dojos=dojos)

@app.route('/ninja-post', methods=['POST'])
def persist_ninja():
    redirectHere = "/dojos/" + request.form['dojo_id']
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age': int(request.form['age'])
    }
    returnedID = Ninja.save_ninja(data)
    return redirect(redirectHere)