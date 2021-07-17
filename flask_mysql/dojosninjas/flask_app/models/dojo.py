from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def select_all(cls):
        query = "SELECT * FROM dojos;"
        db_result_list = connectToMySQL('dojos_and_ninjas').query_db(query)
        listOfDojoObjects = []
        for eachResult in db_result_list:
            makeADojoObject = cls(eachResult)
            listOfDojoObjects.append(makeADojoObject)
        return listOfDojoObjects

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        idOfSavedDojo = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return idOfSavedDojo
    
    @classmethod
    def select_dojo_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        db_result_list = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojoObject = cls(db_result_list[0])
        dojoObject.ninjas = Ninja.select_all_by_dojo_id(data)
        return dojoObject