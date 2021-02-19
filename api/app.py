from flask import Flask, jsonify, make_response, request
from flaskext.mysql import MySQL
from flask_cors import CORS
from pymysql.cursors import DictCursor
from rules import *
from queries import *

app = Flask(__name__)
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
app.config["MYSQL_DATABASE_PORT"] = 3306
app.config["MYSQL_DATABASE_USER"] = 'root'
app.config["MYSQL_DATABASE_PASSWORD"] = 'secret'
app.config["MYSQL_DATABASE_DB"] = 'sheldon'
app.config['MYSQL_CURSORCLASS'] = DictCursor
mysql = MySQL()
mysql.init_app(app)
CORS(app)


@app.route('/top-five-winners')
def top_five_winners():
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute(top_five_query())
        result = cursor.fetchall()

        return jsonify(result)
    except Exception as e:
        return make_response({'result': 'error', 'message': str(e)}, 500)


@app.route('/play-game', methods=['POST'])
def start_game():
    try:
        players = request.get_json()
        con = mysql.get_db()
        cursor = con.cursor()
        player1_id = get_player(cursor, players["player1"]["name"])
        if type(player1_id) != int:
            con.rollback()
            return make_response(player1_id, 500)

        players["player1"]["id"] = player1_id
        player2_id = get_player(cursor, players["player2"]["name"])
        if type(player1_id) != int:
            con.rollback()
            return make_response(player2_id, 500)

        players["player2"]["id"] = player2_id
        result = game_rules(players)
        if result['result'] == 'error':
            con.rollback()
            return make_response(result, 400)

        create_game(cursor, result)
        con.commit()

        return result
    except Exception as e:
        con.rollback()
        return make_response({'result': 'error', 'message': str(e)}, 400)


if __name__ == '__main__':
    app.run()
