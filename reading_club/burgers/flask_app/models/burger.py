from flask_app.config.mysqlconnection import connectToMySQL
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
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db = connectToMySQL('burgers').query_db(query)
        burgers = []
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def save(cls,data):
        query = "Insert INTO burgers (name,bun,meat,calories) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s);"
        burger_id = connectToMySQL('burgers').query_db(query,data)
        return burger_id