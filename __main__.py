import os
import sys
from flask import Flask, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath('user_info.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLALCHEMY_TRACK_MODIFICATIONS deprecated
#app.config['SERVER_NAME'] = '127.0.0.1'
#app.config['SERVER_PORT'] = '5000'
db = SQLAlchemy(app)

def print_err(s):
    print(s, file=sys.stderr)

def generate_page(data):
    with open('include/header.html', 'r') as header:
        page=header.read()
    page += data
    with open('include/footer.html', 'r') as footer:
        page+=footer.read()
    return page

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('include/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('include/css', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('include/fonts', path)

@app.route('/', methods = ["GET", "POST"])
def root():
    if request.method == 'POST':
        # code here         
        db.session.commit() 
    return generate_page(open('include/index.html', 'r').read())

app.run()
