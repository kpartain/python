from flask_app.config.mysqlconnection import connectToMySQL
from .topping import Topping
# burger.py
class Burger:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.toppings = []
    @classmethod

    def get_all_burgers_from_db(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db = connectToMySQL('burgers').query_db(query)
        burgers = []
        for b in burgers_from_db:
            burgers.append(cls(b))
        for burgerObject in burgers:
            responseList = burgerObject.get_one_burgers_toppings(burgerObject.id)
            for eachTopping in responseList:
                toppingObject = Topping(eachTopping['topping_name'])
                burgerObject.toppings.append(burgerObject)
        return burgers

    @classmethod
    def save_a_burger(cls,data):
        query = "Insert INTO burgers (name,bun,meat,calories) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s);"
        burger_id = connectToMySQL('burgers').query_db(query,data)
        return burger_id

    def get_one_burgers_toppings(id):
        query = "SELECT toppings.topping_name FROM many_to_many JOIN toppings ON many_to_many.topping_id = toppings.id WHERE many_to_many.burger_id =%(id);s"
        data = {
            'id': id
        }
        results = connectToMySQL('burgers').query_db(query, data)
        #results will be a list of toppings
        return results