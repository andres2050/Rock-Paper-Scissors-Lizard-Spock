def top_five_query():
    return """
        SELECT p.name, COUNT(g.winner_id) AS wins FROM players AS p
        INNER JOIN games AS g
        ON g.winner_id = p.id
        GROUP BY p.name
        ORDER BY COUNT(g.winner_id) DESC
        LIMIT 5;
    """


def get_player(cursor, player_name):
    query_find = """
        SELECT id FROM players
        WHERE name = %s;
    """

    query_create = """
        INSERT INTO players (name) VALUES (%s);
    """

    cursor.execute(query_find, player_name)
    result = cursor.fetchall()
    if len(result) == 1:
        return result[0]["id"]
    elif len(result) > 1:
        return {'result': 'error', 'message': "Internal error: duplicate results " + player_name}

    cursor.execute(query_create, (player_name,))

    return cursor.lastrowid


def create_game(cursor, result):
    query_create_game = """
        INSERT INTO games (winner_id) VALUES (%s);
    """
    query_create_game_decisions = """
        INSERT INTO game_decisions (player_id, game_id, decision) 
        VALUES 
        (%s, %s, %s),
        (%s, %s, %s);
    """

    winner_id = None
    if result["result"] == 'win':
        winner_id = result["player1"]["id"]
    elif result["result"] == 'lose':
        winner_id = result["player2"]["id"]
    cursor.execute(query_create_game, (winner_id,))
    game_id = cursor.lastrowid

    cursor.execute(query_create_game_decisions, (result["player1"]["id"], game_id, result["player1"]["decision"])
                   + (result["player2"]["id"], game_id, result["player2"]["decision"]))





