from recipes_app import app
from flask import render_template,redirect,request,flash, session
import socket #this is for naughty message
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe

@app.route('/recipes/new')
def add_a_recipe(): 
    if 'user_first_name' not in session:
        return redirect('/')
    print("SESSION INSTRUCTIONS", session['recipe_instructions'])
    return render_template('recipe-form.html')

@app.route('/add-new-recipe-post', methods=['POST'])
def validate_and_persist():
    #returns false or true
    session['recipe_name'] = request.form['name']
    session['recipe_description'] = request.form['description']
    session['recipe_instructions'] = request.form['instructions']
    print("POST SESSION INSTRUCTIONS", session['recipe_instructions'] )
    session['recipe_made_on'] = request.form['date_made']
    result = Recipe.validate_form_data(request.form)
    print("RESULT IN VALIDATE/POST", result)
    if result == False:
        #start recipe useState
        return redirect('/recipes/new')
    else:
        #clear recipe useState
        session['recipe_name'] = ""
        session['recipe_description'] = ""
        session['recipe_instructions'] = ""
        session['recipe_made_on'] = ""
        #persist the recipe
        data = {
            "user_id": session['user_id'],
            "name": request.form['name'],
            "description": request.form['description'],
            "instructions": request.form['instructions'],
            "date_made" : request.form['date_made'],
            "quick": request.form['quick']
        }
        returned_id = Recipe.persist_new_recipe(data)
        return redirect('/success')

@app.route('/recipes/<recipe_id>')
def display_single_recipe(recipe_id):
    if 'user_first_name' not in session:
        return redirect('/')
    data = {
        "id": recipe_id
    }
    result = Recipe.find_recipe_by_id(data)
    if result == False:
        return render_template('notfound.html')
    else: 
        return render_template('recipe-show.html', recipe = result)

@app.route('/recipes/edit/<id>')
def show_edit_form(id):
    #prevent manual navigation to this page if not logged in 
    if 'user_first_name' not in session:
        return redirect('/')
    data = {
        "id" : id
    }
    result = Recipe.find_recipe_by_id(data)
    if result == False:
        return render_template('notfound.html')
    elif result.user_id != session['user_id']:
        #computers name
        hostname = socket.gethostname()
        #IP address affiliated with that computer 
        ipaddress = socket.gethostbyname(hostname)
        session['ip_address'] = ipaddress
        return render_template('disappointed.html')
    else: 
        return render_template('recipe-edit.html', recipe = result)

@app.route('/edit-recipe-post', methods=['POST'])
def validate_and_persist_edit():
    result = Recipe.validate_form_data(request.form)
    if result == False:
        redirect_url = "/recipes/edit/" + request.form['id']
        return redirect(redirect_url)
    else :
        data = {
            "id" : request.form['id'],
            "name" : request.form['name'],
            "description" : request.form['description'],
            "instructions": request.form['instructions'],
            "date_made": request.form['date_made'],
            "quick": request.form['quick']
        }
        response = Recipe.update_existing_recipe(data)
        return redirect("/success")