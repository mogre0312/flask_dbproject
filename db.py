from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:localhost/mydb'
app.config['SQLALCHEMY_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/')
def index():
    fname = 'mogre'
    mail = 'poojaflask@mogre.com'
    entry = User(username = fname, email = mail)
    db.session.add(entry)
    db.session.commit()
    return 'success'

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"