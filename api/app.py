from flask import Flask, jsonify, make_response, request
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
app.config["MYSQL_DATABASE_PORT"] = '3306'
app.config["MYSQL_DATABASE_USER"] = 'root'
app.config["MYSQL_DATABASE_PASSWORD"] = 'secret'
app.config["MYSQL_DATABASE_DB"] = 'sheldon'
app.config["MYSQL_DATABASE_CHARSET"] = 'utf-8'
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def hello_world():
    return {"message": 'Hello World!'}

@app.route('/top-five')
def last_games():
    return {}

@app.route('/start-game', methods=['POST'])
def start_game():
    players = request.get_json()

if __name__ == '__main__':
    app.run()
