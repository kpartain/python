from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.controllers.users import users

if __name__=="__main__":
    app.run(debug=True)