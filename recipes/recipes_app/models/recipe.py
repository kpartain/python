from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#the hashing and validation is removed from server
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

MINIMUM_LENGTH_THREE = re.compile(r'^.{3,1000}$') #password should be 72?
#only letters, no spaces or special characters

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made'] #date submitter made the recipe, NOT created to table
        self.quick = data['quick'] #TINYINT!! 0 = true, 1 = false
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def find_all(cls):
        query = "SELECT * FROM recipes;"
        db_response = connectToMySQL('db1').query_db(query)
        all_recipes = []
        for each_response in db_response:
            make_recipe_object = cls(each_response)
            all_recipes.append(make_recipe_object)
        return all_recipes

    @classmethod
    def validate_form_data(cls, request_form):
        is_valid = True
        rn = request_form['name']
        ds = request_form['description']
        ins = request_form['instructions']
        if not MINIMUM_LENGTH_THREE(rn):
            flash("Recipe name should be three or more characters", "name")
            is_valid = False
        if not MINIMUM_LENGTH_THREE(ds):
            flash("Description should be three or more characters", "description")
            is_valid = False
        if not MINIMUM_LENGTH_THREE(ins):
            flash("Instructions should be three or more characters", "instructions")
            is_valid = False
        
