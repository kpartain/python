from recipes_app import app
from recipes_app.controllers import users
from recipes_app.controllers import recipes

if __name__=="__main__":
    app.run(debug=True)

#pipenv install Flask PyMySQL
#pipenv shell
#pipenv install flask-bcrypt
#python3 server.py

#AWS ******************************
#pipenv lock -r > requirements.txt