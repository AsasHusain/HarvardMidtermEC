from flask import Flask
import db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def hello_world():
    return 'Hello, World!'
