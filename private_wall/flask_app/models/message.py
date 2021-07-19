from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.reipient_id = data['recipient_id']
        self.sender_id = data['sender_id']

    @classmethod
    def get_messages_by_recipient_id(cls, data):
        query = "SELECT * FROM messages WHERE recipient_id = %(id)s;"
        db_response = connectToMySQL('private_wall').query_db(query, data)
        print("msg class find all initial db response", db_response)
        list_of_messages_recieved = []
        for each_response in db_response:
            make_message_object = cls(each_response)
            list_of_messages_recieved.append(make_message_object)
        print("msg class list of msg objs", list_of_messages_recieved)
        return list_of_messages_recieved
    
    @classmethod
    def persist_new_message(cls, data):
        query = "INSERT INTO messages (message, recipient_id, sender_id) VALUES (%(message)s, %(recipient_id)s, %(sender_id)s);"
        returned_msg_id = connectToMySQL('private_wall').query_db(query, data)
        print("persist msg in msg class return ID:", returned_msg_id)
        return returned_msg_id
