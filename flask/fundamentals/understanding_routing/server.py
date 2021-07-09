#in the file, run <pipenv shell> and then <python server.py>
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called 'app'
@app.route('/')          # The '@' decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')
def say_dojo():
    return 'Dojo!'
@app.route('/say/<word>')
def say_word(word):
    return "Hi" + word + "!"
@app.route('/<number>/<word>')
def say_word_x_times(number, word):
    return word * int(number)
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever
if __name__=='__main__':   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.