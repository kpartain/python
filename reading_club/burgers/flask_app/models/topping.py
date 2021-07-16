from flask_app.config.mysqlconnection import connectToMySQL

class Topping:
    def __init__( self , data ):
        self.id = data['id']
        self.topping_name = data['topping_name']
        self.burger_id = data['burger_id']
    @classmethod
    def get_all_toppings(cls):
        query = "SELECT * FROM toppings;"
        #THE DB NAME HERE IS STILL BURGERS, WE ARE QUERYING
        #THE BURGERS DB AT THE TOPPINGS TABLE
        toppings_from_db = connectToMySQL('burgers').query_db(query)
        toppings_list = []
        for eachTopping in toppings_from_db:
            toppingObject = cls(eachTopping)
            toppings_list.append(toppingObject)
        return toppings_list
        
    @classmethod
    def save(cls ,data ):
        query = "INSERT INTO toppings ( topping_name , burger_id) VALUES (%(topping_name)s,%(burger_id)s);"
        return connectToMySQL('burgers').query_db(query,data)