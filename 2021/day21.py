ROLL_COUNTER = 0


def roll(dice_num, dice_outcome=1):
    global ROLL_COUNTER
    ROLL_COUNTER += 1
    dice_num = dice_num + dice_outcome
    if dice_num > 100:
        dice_num = 1
    return dice_num


def play(player, dice_num):
    dice_num = roll(dice_num)
    dice_num1 = dice_num

    dice_num = roll(dice_num)
    dice_num2 = dice_num

    dice_num = roll(dice_num)
    dice_num3 = dice_num

    rolls = dice_num1 + dice_num2 + dice_num3
    player['pos'] = player['pos'] + rolls
    player['pos'] = player['pos'] % 10
    if player['pos'] == 0:
        player['pos'] = 10
    player['score'] += player['pos']
    # rolls_str = f'{dice_num1} {dice_num2} {dice_num3}'
    # print(f"Player {player['name']} rolls {rolls_str} to pos={player['pos']} total score={player['score']}")

    return dice_num


def part1(players, expected_count, max_score):
    dice_num = 0
    global ROLL_COUNTER
    ROLL_COUNTER = 0
    done = False
    looser_score = 0
    while not done:
        dice_num = play(players[1], dice_num)
        if players[1]['score'] > max_score:
            done = True
            looser_score = players[2]['score']
            break
        dice_num = play(players[2], dice_num)
        if players[2]['score'] > max_score:
            done = True
            looser_score = players[1]['score']
            break

    print(f'ROLL_COUNTER={ROLL_COUNTER} looser_score={looser_score}')
    print(ROLL_COUNTER * looser_score)
    assert ROLL_COUNTER * looser_score == expected_count

if __name__ == '__main__':
    # Player 1 starting position: 4
    # Player 2 starting position: 8
    players = {1:{'name':1, 'pos':4, 'score':0}, 2:{'name':2, 'pos':8, 'score':0}}
    part1(players, expected_count=739785, max_score=999)

    # From input data
    # Player 1 starting position: 1
    # Player 2 starting position: 3
    players = {1:{'name':1, 'pos':1, 'score':0}, 2:{'name':2, 'pos':3, 'score':0}}
    part1(players, expected_count=897798, max_score=999)

    # print(sys.maxsize)
#    444356092776315
#    2147483647