from flask_app.config.mysqlconnection import connectToMySQL
import re

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        #password?

    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
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