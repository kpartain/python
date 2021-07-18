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
        #password?

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
        if fn.isAlpha() is True and len(fn) < 2:
            flash("First name should be two characters or longer")
            is_valid = False
        #last_name
        if ln.isalpha() is False and len(fn) < 2:
            flash("First name should be at least two characters and only include letters")
            is_valid = False
        if ln.isalpha() is False and len(fn) >= 2:
            flash("First name should only include letters")
            is_valid = False
        if ln.isAlpha() is True and len(fn) < 2:
            flash("First name should be two characters or longer")
            is_valid = False
        #password
        if len(pw) < 8:
            flash("Password must be more than 8 characters")
            is_valid = False
        return is_valid
        
    @classmethod
    def add_new_user(cls, data):
        #validate user data
        #save to DB
        #return user object to session
        return true

    @classmethod
    def get_registered_user(cls, data):
        #validate user data
        #get data from DB
        query = "SELECT user.first_name, user.last_name FROM users WHERE "
        #return user object to session
        return true

    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where lower(email) LIKE %(email)s;"
        