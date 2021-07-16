from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger

@app.route('/')
def index():
    return render_template("index.html",burgers=Burger.get_all())

@app.route('/create',methods=['POST'])
def make_burgers():
    data = {
            "name" : request.form['name'],
            "bun" : request.form['bun'],
            "meat" : request.form['meat'],
            "calories" : request.form['calories']
        }
    Burger.save(data)
    return redirect('/burgers')

@app.route('/burgers')
def all_burgers():
    return render_template("results.html",burgers=Burger.get_all())
