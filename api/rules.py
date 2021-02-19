def game_rules(players):
    rules = {
        'rock': {'lizard': 'crushes', 'scissors': 'crushes'},
        'paper': {'rock': 'covers', 'spock': 'disproves'},
        'scissors': {'paper': 'cuts', 'lizard': 'decapitates'},
        'lizard': {'spock': 'poisons', 'paper': 'eats'},
        'spock': {'scissors': 'smashes', 'rock': 'vaporizes'}
    }

    decision1 = players["player1"]["decision"]
    decision2 = players["player2"]["decision"]
    if decision1 in rules and decision2 in rules:
        if decision1 == decision2:
            return {**players, 'result': 'equal', 'message': 'equal'}
        elif decision2 in rules[decision1]:
            return {**players, 'result': 'win', 'message': rules[decision1][decision2]}
        elif decision1 in rules[decision2]:
            return {**players, 'result': 'lose', 'message': rules[decision2][decision1]}

    return {'result': 'error', 'message': 'invalid game decision'}
