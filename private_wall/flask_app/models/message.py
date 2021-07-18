from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.reipient_id = data['recipient_id']
        self.sender_id = data['sender_id']

    @classmethod
    def get_messages_by_sender_id():
        query = "SELECT * FROM messages WHERE "