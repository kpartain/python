#pipenv install flask requests  [you can do all your installs in one line seperated by space]
#pipenv shell
#python ____.py (server)
from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def home_page():
    recvd = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    #if you want to see what is available in the response object to write your keys
    # print(recvd)
    # for each in recvd:
    #     print(each)
    jsonObj = recvd.json()
    print(jsonObj['height'])
    return render_template('index.html', jsonObj = jsonObj)

if __name__=="__main__":
    app.run(debug=True)