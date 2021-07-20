from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
#the hashing and validation is removed from server
from recipes_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#8 is the minimum, the 255 is the upper bound - change to DB max.
MINIMUM_LENGTH_TWO = re.compile(r'^.{2,1000}$')
#8 is the minimum, the 255 is the upper bound - change to DB max. 255 is safe
MINIMUM_LENGTH_EIGHT = re.compile(r'^.{8,1000}$') #password should be 72?
#only letters, no spaces or special characters
LETTERS_ONLY = re.compile(r'^[a-zA-Z]+$')
#letters and dash/hyphen/dot but NO SPACES
LETTERS_CHARS_NO_SPACE = re.compile(r'^[A-Za-z]+(((\'|\-|\.)?([A-Za-z])+))?$')
#letters and spaces (two names with a space) and dash/hyphen/dot
LETTERS_CHARS_SPACE = re.compile(r'^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$')
#letters and spaces but no special chars
LETTERS_SPACE_NO_CHARS = re.compile(r'^[A-Za-z]+((\s)?([A-Za-z])+)*$')
#to add a character (ex: underscore), change (\'|\-|\.) to (\'|\-|\.|\_) 

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made'] #date submitter made the recipe, NOT created to table
        self.quick = data['quick'] #boolean T/F, T if under 30 min
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
