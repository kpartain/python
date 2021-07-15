# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('friends_db').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            newFriend = cls(friend)
            friends.append(newFriend)
        return friends
    def update_one(cls, newName, idNum):
        query = "UPDATE friends SET first_name=%(newName)s WHERE id=%(idNum)s;"
        data = {
            "newName": request.form['newName'],#possibly a value from a form
            "idNum": request.form['idNum']#possibly a value from the URL
            } 
        mysql.query_db(query, data)
        return "updated name!"
    def find_by_name(cls, findName):
        query = "SELECT * from friends WHERE first_name = %(findName)s;"
        data = {
            'findName': request.form['email']
        }
        result = mysql.query_db(query, data)
        matchFriend = cls(result)
        return matchFriend
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db( query, data )