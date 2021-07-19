from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.reipient_id = data['recipient_id']
        self.sender_id = data['sender_id']
        #does this work?? ^
        self.sender_name = data['sender_name']
        self.created_at = data['created_at']

    @classmethod
    def get_messages_by_recipient_id(cls, data):
        query = "SELECT *, users.first_name as 'sender_name' FROM messages JOIN users ON messages.sender_id = users.id WHERE recipient_id = %(id)s"
        db_response = connectToMySQL('private_wall').query_db(query, data)
        print("msg class find all initial db response", db_response)
        #here is new data for sender_name
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

    @classmethod
    def get_count_of_sent_messages(cls, data):
        query = "SELECT COUNT(messages.sender_id) as number_sent FROM messages WHERE messages.sender_id = %(id)%;"
        db_response = connectToMySQL('private_wall').query_db(query, data)
        print("db response for num sent from cls mthd", db_response)
        print("accessing key for return", db_response['number_sent'])
        return db_response['number_sent']