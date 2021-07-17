from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def select_all(cls):
        query = "SELECT * FROM ninjas;"
        db_result_list = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        listOfNinjaObjects = []
        for eachResult in db_result_list:
            makeANinjaObject = cls(eachResult)
            listOfNinjaObjects.append(makeANinjaObject)
        return listOfNinjaObjects

    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        idOfSavedNinja = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return idOfSavedNinja

    @classmethod
    def select_all_by_dojo_id(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(id)s;"
        db_result_list = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        listOfNinjaObjectsByDojoID = []
        for eachResult in db_result_list:
            makeANinjaObject = cls(eachResult)
            listOfNinjaObjectsByDojoID.append(makeANinjaObject)
        return listOfNinjaObjectsByDojoID