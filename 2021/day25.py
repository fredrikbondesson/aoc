import copy

INPUT="""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

def check_and_move_cucumber(cucumber_to_move, row_nr, col_nr, board, orig_board):
    if orig_board[row_nr][col_nr] == cucumber_to_move:
        if cucumber_to_move == '>':
            posy = row_nr
            posx = col_nr + 1
            if posx > len(board[0]) - 1:
                posx = 0

            if orig_board[posy][posx] == '.':
                board[posy][posx] = cucumber_to_move
                board[row_nr][col_nr] = '.'
                #print(f"Moving {cucumber_to_move} from {row_nr}, {col_nr} to {posy}, {posx}")

        if cucumber_to_move == 'v':
            posy = row_nr + 1
            posx = col_nr
            if posy > len(board) - 1:
                posy = 0

            if orig_board[posy][posx] == '.':
                board[posy][posx] = cucumber_to_move
                board[row_nr][col_nr] = '.'
                #print(f"Moving {cucumber_to_move} from {row_nr}, {col_nr} to {posy}, {posx}")


def run(data):
    board = copy.deepcopy(data)
    orig_board = copy.deepcopy(data)

    counter = 1
    done = False
    while not done:
        for row_nr, row in enumerate(orig_board):
            for col_nr, cucumber in enumerate(row):
                check_and_move_cucumber('>', row_nr, col_nr, board, orig_board)

        if orig_board == board:
            done = True
        orig_board = copy.deepcopy(board)

        for row_nr, row in enumerate(orig_board):
            for col_nr, cucumber in enumerate(row):
                check_and_move_cucumber('v', row_nr, col_nr, board, orig_board)

        if orig_board == board and done == True:
            done = True
            return counter
        else:
            done = False

        counter += 1
        orig_board = copy.deepcopy(board)

    return None

def get_board(data):
    board = []
    for row in data:
        buf = []
        for val in row:
            buf.append(val)

        board.append(buf)
    return board


def main():
    rows = INPUT.rstrip().split('\n')
    print(rows)
    board = get_board(rows)
    step = run(board)
    print('final step:', step)
    assert step == 58

    data = open('2021/day25.txt').read().strip().split('\n')

    board = get_board(data)
    step = run(board)
    print('final step:', step)
    assert step == 518


if __name__ == '__main__':
    main()