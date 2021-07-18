from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
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
    def validate_user(form_data):
        is_valid = True
        fn = form_data['first_name'].strip()
        ln = form_data['last_name'].strip()
        em = form_data['email'].strip()
        pw = form_data['password']
        # email
        if not EMAIL_REGEX.match(em): 
            flash("Invalid email address!")
            is_valid = False
        #first_name
        if fn.isalpha() is False and len(fn) < 2:
            flash("First name should be at least two characters and only include letters")
            is_valid = False
        if fn.isalpha() is False and len(fn) >= 2:
            flash("First name should only include letters")
            is_valid = False
        if fn.isalpha() is True and len(fn) < 2:
            flash("First name should be two characters or longer")
            is_valid = False
        #last_name
        if ln.isalpha() is False and len(fn) < 2:
            flash("First name should be at least two characters and only include letters")
            is_valid = False
        if ln.isalpha() is False and len(fn) >= 2:
            flash("First name should only include letters")
            is_valid = False
        if ln.isalpha() is True and len(fn) < 2:
            flash("First name should be two characters or longer")
            is_valid = False
        #password
        if len(pw) < 8:
            flash("Password must be more than 8 characters")
            is_valid = False
        return is_valid
    
    @classmethod
    def register_and_login(cls, data):
        returned_id = User.add_new_user(data)
        user_obj = User.get_registered_user_by_id(returned_id)
        print("register and login result object", user_obj)
        return user_obj

    @classmethod
    def add_new_user(cls, data):
        #save to DB with query
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        db_result = connectToMySQL('registration').query_db(query, data)
        print("Add new user result", db_result)
        #return user ID which is returned from query
        return db_result

    @classmethod
    def get_registered_user_by_id(cls, data):
        #get data from DB
        dict = {
            "id": data
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"
        db_response = connectToMySQL('registration').query_db(query, dict)
        user_obj = cls(db_response[0])
        print("get registered user obj result", user_obj)
        #return user object to session
        return user_obj

    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where lower(email) LIKE %(email)s;"
        db_response = connectToMySQL('registration').query_db(query, data)
        print("DBResp get by email", db_response)
        if len(db_response) != 1:
            return False
        else: 
            return cls(db_response[0])
        