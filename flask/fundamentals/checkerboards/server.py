#if you don't have pipfile and pipfile.lock, run pipenv install flask
#after, to boot your server:
#enter into the shell <pipenv shell>
#and then start the server <python server.py>
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called 'app'
@app.route('/')          # The '@' decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', width=10, height=10)# Return the string 'Hello World!' as a response
@app.route('/4')
def four():
    return render_template('index.html', width=10, height=4)
@app.route('/<height>/<width>')
def h_and_w(height, width):
    y = int(height)
    x = int(width)
    return render_template('index.html', width=x, height=y)
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever
if __name__=='__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.