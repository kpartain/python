#if you don't have pipfile and pipfile.lock, run pipenv install flask
#after, to boot your server:
#enter into the shell <pipenv shell>
#and then start the server <python server.py>
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called 'app'
# @app.route('/normal')          # The '@' decorator associates this route with the function immediately following
# def eight_eight_default(width, height):
#     return render_template('index.html', width=8, height=8)
# @app.route('/4')
# def eight_four():
#     return render_template('index.html', width=8, height=4)
@app.route('/<x>/<y>')
def x_by_y(x,y):
    width = int(x)
    height = int(y)
    return render_template('index.html', width=width, height=height)
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever
if __name__=='__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.