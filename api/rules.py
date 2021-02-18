def game_rules(decision1, decision2):
    if decision1 == decision2:
        return {'result': 'equal', 'message': 'equal'}

    rules = {
        'stone': {'lizard': 'crushes', 'scissors': 'crushes'},
        'paper': {'stone': 'covers', 'spock': 'disproves'},
        'scissors': {'paper': 'cuts', 'lizard': 'decapitates'},
        'lizard': {'spock': 'poisons', 'paper': 'eats'},
        'spock': {'scissors': 'smashes', 'stone': 'vaporizes'}
    }

    if decision1 in rules and decision2 in rules:
        if decision2 in rules[decision1]:
            return {'result': 'win', 'message': rules[decision1][decision2]}
        elif decision1 in rules[decision2]:
            return {'result': 'lose', 'message': rules[decision2][decision1]}

    return {'result': 'error', 'message': 'invalid game decision'}
