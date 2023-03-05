from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'
mysql= MySQL(app)


@app.route("/")
def index():
    firstname = 'Pooja'
    lastname = 'Mogre'
    cur= mysql.connection.cursor()
    cur.execute('''SELECT * FROM users''')
    rv = cur.fetchall()
    return str(rv)
    # cur.execute('INSERT INTO users(fname, lname) VALUES (%s, %s)', (firstname, lastname))
    # mysql.connection.commit()
    # cur.close()
    # return 'success'

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

