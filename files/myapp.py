from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://amit:password@localhost/flask_db'
db = SQLAlchemy(app)

from one_to_many import *

if __name__ == "__main__":
    app.run(debug=True)