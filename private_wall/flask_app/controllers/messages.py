from flask_app import app
from flask import render_template,redirect,request,flash, session
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/wall')
def show_messages():
    data = {
        "id": session['user_id']
    }
    list_of_messages = Message.get_messages_by_recipient_id(data)
    return render_template('success.html', list_of_messages = list_of_messages)

@app.route('/new-message-post-request', methods=['POST'])
def send_the_message():
    data = {
        "message" : request.form['message'],
        "recipient_id" : request.form['recipient_id'],
        "sender_id" : request.form['sender_id']
    }
    returned_message_ID = Message.persist_new_message(data)
    return redirect('/wall')