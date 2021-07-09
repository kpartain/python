#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def foo():
    return render_template('index.html')
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)