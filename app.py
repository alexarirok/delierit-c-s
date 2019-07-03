import os
from flask import Flask  

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def home():
    return "Welcome Home!"

@app.route('/<about>')
def about_home(about):
    return "Welcome {}!".format(about)

if __name__ == '__main__':
    app.run(debug=True)