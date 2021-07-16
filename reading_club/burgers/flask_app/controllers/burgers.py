from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.burger import Burger
from flask_app.models.topping import Topping

@app.route('/')
def index():
    currentToppings = Topping.get_all_toppings()
    return render_template("index.html", allCurrentToppings = currentToppings)

@app.route('/create',methods=['POST'])
def make_burgers():
    #is toppings none? 
    data = {
            "name" : request.form['name'],
            "bun" : request.form['bun'],
            "meat" : request.form['meat'],
            "calories" : request.form['calories']
        }
    #save it, recall the save method returns the saved burger ID
    returnID = Burger.save_a_burger(data)
    #we will use the returned ID to save the toppings
    #WE ONLY WANT TO DO THIS IF BURGERID IS NOT NULL!
    if request.form['BURGERID'] is not None: 
        top_data = {
            'burger_id': returnID,
            'id': request.form['topping_name']
        }
        Topping.save(top_data)
    return redirect('/burgers')

@app.route('/burgers')
def all_burgers():
    allBurgers = Burger.get_all_burgers_from_db()
    return render_template("results.html",burgers=allBurgers)
