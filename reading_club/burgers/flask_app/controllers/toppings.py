from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger

@app.route('/topping-form')
def display_form():
    #we will hand this page the burgers so we can use radio
    #buttons to select which burger to add a topping to
    return render('topping_form.html', burgers=Burger.get_all())

@app.route('/add-toppings',methods=['POST'])
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
