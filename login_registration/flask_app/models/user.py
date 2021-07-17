

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        #password?
    
    @classmethod
    def add_new_user(cls, data):
        #validate user data
        #save to DB
        #return user object to session

    @classmethod
    def get_registered_user(cls, data):
        #validate user data
        #get data from DB
        #return user object to session