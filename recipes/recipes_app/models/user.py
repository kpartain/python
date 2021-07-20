from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#the hashing and validation is removed from server
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]+$')
MINIMUM_LENGTH_TWO = re.compile(r'^.{2,255}$') #the 2 is the minimum, the 255 is the upper bound - change to DB max.
MINIMUM_LENGTH_EIGHT = re.compile(r'^.{8,255}$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
        elif User.get_by_email(form_data['email']) is True:
            flash("This email is registered to an account, please log in", "email")
        #first_name
        if LETTERS_ONLY.match(fn) is False and MINIMUM_LENGTH_TWO.match(fn) is False:
            flash("First name should be at least two characters and only include letters", "first_name")
            is_valid = False
        elif LETTERS_ONLY.match(fn) is False and MINIMUM_LENGTH_TWO.match(fn) is True:
            flash("First name should only include letters", "first_name")
            is_valid = False
        elif LETTERS_ONLY.match(fn) is True and MINIMUM_LENGTH_TWO.match(fn) is False:
            flash("First name should be two characters or longer", "first_name")
            is_valid = False
        #last_name
        if LETTERS_ONLY.match(ln) is False and MINIMUM_LENGTH_TWO.match(ln) is False:
            flash("Last name should be at least two characters and only include letters", "last_name")
            is_valid = False
        elif LETTERS_ONLY.match(ln) is False and MINIMUM_LENGTH_TWO.match(ln) is True:
            flash("Last name should only include letters", "last_name")
            is_valid = False
        elif LETTERS_ONLY.match(ln) is True and MINIMUM_LENGTH_TWO.match(ln) is False:
            flash("Last name should be two characters or longer", "last_name")
            is_valid = False
        #password
        if MINIMUM_LENGTH_EIGHT.match(pw) is False and pw == pw2:
            flash("Password must be at least 8 characters", "password")
            is_valid = False
        elif MINIMUM_LENGTH_EIGHT.match(pw) is True and pw != pw2:
            flash("Passwords must match!", "password")
            is_valid = False
        elif MINIMUM_LENGTH_EIGHT.match(pw) is False and pw != pw2:
            flash("Passwords must be at least 8 characters and match.", "password")
            is_valid = False
        return is_valid

    #returns false if any errors or returns the object if registered and saved
    @classmethod
    def register_and_login(cls, request_form):
        if User.validate_registration(request_form) is False:
            return False
        else:
            data = {
            "first_name": request_form['first_name'],
            "last_name": request_form['last_name'],
            "email": request_form['email'],
            "password" : bcrypt.generate_password_hash(request_form['password'])
            }
            returned_id = User.add_new_user(data)
            user_obj = User.get_registered_user_by_id(returned_id['id'])
            return user_obj
    

    #returns false if any errors or returns the object if logged in 
    @staticmethod
    def validate_login(form_data):
        is_valid = True
        #returns false if not found, returns the object if found
        result = User.get_by_email(form_data['login_email'])
        if user_object is False:
            flash("Invalid email and/or password.", "login")
            is_valid = False
        elif not bcrypt.check_password_hash(result.password, form_data['login_password']):
            flash("Invalid email and/or password.", "login")
            is_valid = False
        if is_valid == True:
            return result
    
    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        db_result = connectToMySQL('registration').query_db(query, data)
        return db_result

    @classmethod
    def get_registered_user_by_id(cls, data):
        dict = {
            "id": data
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        db_response = connectToMySQL('registration').query_db(query, dict)
        user_obj = cls(db_response[0])
        return user_obj

    #returns false if nothing found or returns the object
    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where lower(email) LIKE %(email)s;"
        db_response = connectToMySQL('registration').query_db(query, data)
        print("DBResp get by email", db_response)
        if len(db_response) != 1:
            return False
        else: 
            user_obj = cls(db_response[0])
            return user_obj
        