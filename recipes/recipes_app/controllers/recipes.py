from recipes_app import app
from flask import render_template,redirect,request,flash, session
from recipes_app.models.user import User
from recipes_app.models.recipe import Recipe

@app.route('/recipes/new')
def add_a_recipe():
    return render_template('recipe-form.html')

@app.route('/add-new-recipe-post', methods=['POST'])
def validate_and_persist():
    #returns false or true
    result = Recipe.validate_form_data(request.form)
    if result == False:
        #start recipe useState
        session['recipe_name'] = request.form['name']
        session['recipe_description'] = request.form['description']
        session['recipe_instructions'] = request.form['instructions']
        session['recipe_made_on'] = request.form['date_made']
        return redirect('/')
    else:
        #clear recipe useState
        session['recipe_name'] = request.form['name']
        session['recipe_description'] = request.form['description']
        session['recipe_instructions'] = request.form['instructions']
        session['recipe_made_on'] = request.form['date_made']
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