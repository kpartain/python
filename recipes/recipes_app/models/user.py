from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#the hashing and validation is removed from server
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#8 is the minimum, the 255 is the upper bound - change to DB max.
MINIMUM_LENGTH_TWO = re.compile(r'^.{2,255}$')
#8 is the minimum, the 255 is the upper bound - change to DB max.
MINIMUM_LENGTH_EIGHT = re.compile(r'^.{8,255}$')
#only letters, no spaces or special characters
LETTERS_ONLY = re.compile(r'^[a-zA-Z]+$')
#letters and dash/hyphen/dot but NO SPACES
LETTERS_CHARS_NO_SPACE = re.compile(r'^[A-Za-z]+(((\'|\-|\.)?([A-Za-z])+))?$')
#letters and spaces (two names with a space) and dash/hyphen/dot
LETTERS_CHARS_SPACE = re.compile(r'^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$')
#letters and spaces but no special chars
LETTERS_SPACE_NO_CHARS = re.compile(r'^[A-Za-z]+((\s)?([A-Za-z])+)*$')
#to add a character (ex: underscore), change (\'|\-|\.) to (\'|\-|\.|\_) 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        #consider using form_data['foo'].strip() to remove whitespace
        fn = form_data['first_name']
        ln = form_data['last_name']
        em = form_data['email']
        pw = form_data['password']
        pw2 = form_data['confirm_password']
        #email LETTERS_ONLY.match(fn)
        if not EMAIL_REGEX.match(em): 
            flash("Invalid email address!", "email")
            is_valid = False
        # if User.get_by_email(form_data['email']) == True:
        #     flash("This email is registered to an account, please log in", "email")
        #     is_valid = False
        #first_name
        if not LETTERS_ONLY.match(fn) and not MINIMUM_LENGTH_TWO.match(fn):
            flash("First name should be at least two characters and only include letters", "first_name")
            is_valid = False
        elif not LETTERS_ONLY.match(fn) and MINIMUM_LENGTH_TWO.match(fn):
            flash("First name should only include letters", "first_name")
            is_valid = False
        elif LETTERS_ONLY.match(fn) and not MINIMUM_LENGTH_TWO.match(fn):
            flash("First name should be two characters or longer", "first_name")
            is_valid = False
        #last_name
        if not LETTERS_ONLY.match(ln) and not MINIMUM_LENGTH_TWO.match(ln):
            flash("Last name should be at least two characters and only include letters", "last_name")
            is_valid = False
        elif not LETTERS_ONLY.match(ln) and MINIMUM_LENGTH_TWO.match(ln):
            flash("Last name should only include letters", "last_name")
            is_valid = False
        elif LETTERS_ONLY.match(ln) and not MINIMUM_LENGTH_TWO.match(ln):
            flash("Last name should be two characters or longer", "last_name")
            is_valid = False
        #password
        if not MINIMUM_LENGTH_EIGHT.match(pw) and pw == pw2:
            flash("Password must be at least 8 characters", "password")
            is_valid = False
        elif MINIMUM_LENGTH_EIGHT.match(pw) and pw != pw2:
            flash("Passwords must match!", "password")
            is_valid = False
        elif not MINIMUM_LENGTH_EIGHT.match(pw) and pw != pw2:
            flash("Passwords must be at least 8 characters and match.", "password")
            is_valid = False
        return is_valid

    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        db_result = connectToMySQL('db1').query_db(query, data) #should return the rowid as just an int
        return db_result


    #returns false if any errors or returns the object if registered and saved
    @classmethod
    def register_and_login(cls, request_form):
        if User.validate_registration(request_form) is False:
            return False
        else:
            hashed_pw = bcrypt.generate_password_hash(request_form['password'])
            data = {
            "first_name": request_form['first_name'],
            "last_name": request_form['last_name'],
            "email": request_form['email'],
            "password" : hashed_pw
            }
            returned_id = User.add_new_user(data)
            user_obj = User.get_registered_user_by_id(returned_id) #connection query should return an int?
            return user_obj
    
    #returns user object
    @classmethod
    def get_registered_user_by_id(cls, data):
        dict = {
            "id": data
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        db_response = connectToMySQL('db1').query_db(query, dict)
        user_obj = cls(db_response[0])
        return user_obj

    #returns false if nothing found or returns the object
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        db_response = connectToMySQL('db1').query_db(query, data)
        print("DBResp get by email", db_response)
        if len(db_response) == 0:
            print("Email not found")
            return False
        else: 
            user_obj = cls(db_response[0])
            return user_obj
        
    #returns false if any errors or returns the object if logged in 
    @staticmethod
    def validate_login(form_data):
        is_valid = True
        #returns false if not found, returns the object if found
        data = {
            "email" : form_data['login_email']
        }
        result = User.get_by_email(data)
        if result is False:
            flash("Invalid email and/or password.", "login")
            is_valid = False
            return False
        else :
            if not bcrypt.check_password_hash(result.password, form_data['login_password']):
                flash("Invalid email and/or password.", "login")
                is_valid = False
            if is_valid == True:
                return result
            else:
                return is_valid