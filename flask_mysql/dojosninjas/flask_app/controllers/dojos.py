from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from datetime import datetime, timedelta

@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.select_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/dojo-post', methods=['POST'])
def persist_dojo():
    data = {
        'name': request.form['name']
    }
    returnedID = Dojo.save_dojo(data)
    return redirect("/dojos")

@app.route('/dojos/<dojo_id>')
def show_dojo_and_its_ninjas(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.select_dojo_by_id(data)
    ninjas = dojo.ninjas
    created = ninjas[0].updated_at
    current = datetime.now()
    diff = current - created
    diff2 = diff.seconds
    hours, remainder = divmod(diff2, 3600)
    minutes, seconds = divmod(remainder, 60)
    number_of_days_string = diff.days, "days ago"
    formatted_hours_minutes_seconds = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    message_for_HTML = ""
    if diff.days > 0 : 
        message_for_HTML = 'more than a day ago'
    if diff.days == 0 and diff.hours > 0 : 
        message_for_HTML = diff.hours, " hours ago"
    if diff.days == 0 and diff.hours == 0 :
        message_for_HTML = diff.minutes, " minutes ago"
    if diff.days == 0 and diff.hours == 0 and diff.minutes == 0:
        message_for_HTML = "less than a minute ago"
    return render_template('dojo-show.html', dojo = dojo, ninjas = ninjas, diff = diff, message_for_HTML = message_for_HTML, current = current, created = created)