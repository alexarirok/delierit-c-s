import os
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Result

@app.route('/')
def home():
    return "Welcome Home!"

@app.route('/<about>')
def about_home(about):
    return "Welcome {}!".format(about)

if __name__ == '__main__':
    app.run(debug=True)