from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fullName = self.first_name + " " + self.last_name
        
    @classmethod
    def get_all_users(cls):
        query = "SELECT * from users;"
        db_response = connectToMySQL('users_schema').query_db(query)
        listOfUserClassObjects = []
        for eachDBRow in db_response:
            newUserClassObject = cls(eachDBRow)
            listOfUserClassObjects.append(newUserClassObject)
        return listOfUserClassObjects

    @classmethod
    def add_new_user(cls, data):
        #if your DB does not populate created/updated, add these
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        saved_user_ID = connectToMySQL('users_schema').query_db(query, data)
        return saved_user_ID

    @classmethod
    def get_single_user(cls, data):
        query = "SELECT * from users WHERE users.id = %(id)s;"
        db_response = connectToMySQL('users_schema').query_db(query, data)
        #this returns a list with only one response so we need to use index 
        singleClassObject = cls(db_response[0])
        return singleClassObject

    @classmethod
    def update_single_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_user_from_db(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('users_schema').query_db(query, data)
