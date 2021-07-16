from flask_app.config.mysqlconnection import connectToMySQL

class Topping:
    def __init__( self , data ):
        self.id = data['id']
        self.topping_name = data['topping_name']
        self.burger_id = data['burger_id']
    @classmethod
    def save(cls ,data ):
        query = "INSERT INTO toppings ( topping_name , burger_id) VALUES (%(topping_name)s,%(burger_id)s);"
        return connectToMySQL('burgers').query_db(query,data)