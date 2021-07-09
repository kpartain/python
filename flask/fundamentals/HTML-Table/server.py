#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def foo():
    return render_template('index.html')
@app.route('/list')
def renderList():
    users_dict = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users = users_dict)
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)