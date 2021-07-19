from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from message import Message
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
        self.recieved_messages= []
        self.sent_messages = []

    @staticmethod
    def validate_user(form_data):
        is_valid = True
        lower_case_email = form_data["email"].lower()
        email_data = { 
            "email" : lower_case_email
        }
        user_in_db = User.get_by_email(email_data)
        print("UserinDB", user_in_db)
        #if user in DB, return a message asking them to log in
        if user_in_db is True :
            flash("This email is already registered to an account - please log in.")
            is_valid = False
        fn = form_data['first_name'].strip()
        ln = form_data['last_name'].strip()
        em = form_data['email'].strip()
        pw = form_data['password']
        pw2 = form_data['confirm_password']
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
            flash("Last name should be at least two characters and only include letters")
            is_valid = False
        if ln.isalpha() is False and len(fn) >= 2:
            flash("Last should only include letters")
            is_valid = False
        if ln.isalpha() is True and len(fn) < 2:
            flash("Last name should be two characters or longer")
            is_valid = False
        #password
        if len(pw) < 8:
            flash("Password must be more than 8 characters")
            is_valid = False
        if pw != pw2:
            flash("Passwords must match!")
            is_valid = False
        return is_valid
    
    @classmethod
    def register_and_login(cls, data):
        returned_id = User.add_new_user(data)
        print("register and login result ID", returned_id)
        user_obj = User.get_registered_user_by_id(returned_id)
        print("register and login result object", user_obj)
        return user_obj

    @classmethod
    def add_new_user(cls, data):
        #save to DB with query
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        db_result = connectToMySQL('private_wall').query_db(query, data)
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
        db_response = connectToMySQL('private_wall').query_db(query, dict)
        user_obj = cls(db_response[0])
        print("get registered user obj result", user_obj)
        user_obj.recieved_messages = user_obj.get_this_users_recieved_messages(user_obj.id)
        print("get registered user and messages", user_obj)
        #return user object to session
        return user_obj

    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where lower(email) LIKE %(email)s;"
        db_response = connectToMySQL('private_wall').query_db(query, data)
        print("DBResp get by email", db_response)
        if len(db_response) != 1:
            return False
        else: 
            user_object = cls(db_response[0])
            print("get by email object", user_object)
            user_object.recieved_messages = Message.get_this_users_recieved_messages(user_object.id)
            print("get by email object with msgs", user_object)
            return user_object
    
    @classmethod
    def get_this_users_recieved_messages(cls, data):
        #controller will hand this data of the logged in user's ID
        recieved_messages = Message.get_messages_by_recipient_id(data)
        print("recieved msgs in user class", recieved_messages)
        return recieved_messages