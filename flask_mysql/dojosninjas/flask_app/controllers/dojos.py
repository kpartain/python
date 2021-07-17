from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.select_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojo-post', methods=['POST'])
def persist_dojo():
    data = {
        'name': request.form['name']
    }
    returnedID = Dojo.save_dojo(data)
    return redirect("/dojos")

@app.route('/dojos/<dojo_id>')
def show_dojo_and_its_ninjas(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.select_dojo_by_id(data)
    ninjas = dojo.ninjas
    return render_template('dojo-show.html', dojo = dojo, ninjas = ninjas)