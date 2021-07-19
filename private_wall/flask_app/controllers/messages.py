from flask_app import app
from flask import render_template,redirect,request,flash, session
import socket
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/wall')
def show_messages():
    #computers name
    hostname = socket.gethostname()
    #IP address affiliated with that computer 
    ipaddress = socket.gethostbyname(hostname)
    session['ip_address'] = ipaddress
    #get all users for right side of page to send
    all_users = User.get_all_users()
    print("before removing logged in user", all_users)
    for each_user in all_users:
        if (each_user.id == session['user_id']):
            all_users.remove(each_user)
    print("Did this remove current user from list?", all_users)
    #get all messages for current logged in user for left side of page
    data = {
        "id": session['user_id']
    }
    number_of_messages_sent = Message.get_count_of_sent_messages(data)
    print("Number of sent messages:", number_of_messages)
    list_of_messages = Message.get_messages_by_recipient_id(data)
    number_of_messages = len(list_of_messages)
    return render_template('success.html', number_of_messages = number_of_messages, number_of_messages_sent = number_of_messages_sent, list_of_messages = list_of_messages, list_of_other_users = all_users)

@app.route('/<sender_id>/to/<recipient_id>', methods=['POST'])
def send_the_message(sender_id, recipient_id):
    #check if someone is manually trying to send a message using someone else's ID
    if sender_id != session['user_id']:
        session['hacker_confirmed'] = "You're not user ID",sender_id,", you can't send messages from someone else's account!"
        return redirect('/nice-try')
    #
    #otherwise, send the message
    data = {
        "message" : request.form['message'],
        "recipient_id" : recipient_id,
        "sender_id" : session['user_id']
    }
    returned_message_ID = Message.persist_new_message(data)
    print("Message sent! Returned ID:",returned_message_ID)
    return redirect('/wall')

@app.route('/delete-this-message/<message_id>')
def delete_this_message(message_id):
    data = {
        "id": session['user_id']
    }
    list_of_messages = Message.get_messages_by_recipient(data)
    able_to_delete = False
    for each_message in list_of_messages:
        if (each_message.id == message_id):
            able_to_delete = True
            break
    if able_to_delete is False:
        session['hacker_confirmed'] = "Hey,",message_id,"isn't your message to delete!!"
        return redirect('/nice-try')
    elif able_to_delete is True:
        message_data = {
            "id": message_id
        }
        Message.delete_a_message(message_data)
        return redirect('/success')

@app.route('/nice-try')
def ah_ah_ah_you_didnt_say_the_magic_word():
    return render_template('disappointed.html')