from typing import List
import util


INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

BOARD_SIZE = 5


class Board():

    def __init__(self, rows) -> None:
        self._board = []
        self._marked = []
        assert len(rows) == BOARD_SIZE
        for row in rows:
            self._board.append(row.split())
            self._marked.append(BOARD_SIZE * [0])

    def __str__(self) -> str:
        result = ''
        for row in self._board:
            result += str(row) + "\n"
        return result

    def check(self, val: int):
        for row_idx, row in enumerate(self._board):
            for col_idx, value in enumerate(row):
                if val == value:
                    # print(f'found {nr} in {row_idx} {col_idx}')
                    self._marked[row_idx][col_idx] = 'X'

        if self._check():
            return True

    def _check(self):
        for idx, row in enumerate(self._marked):
            if len([x for x in row if x=='X']) == BOARD_SIZE:
                return True

            # TODO Fix
            pelle = [self._marked[0][idx], self._marked[1][idx], self._marked[2][idx],
                    self._marked[3][idx], self._marked[4][idx]]
            if len([x for x in pelle if x=='X']) == BOARD_SIZE:
                return True

    def get_sum_unmarked(self):
        unmarked = 0
        for row_idx, row in enumerate(self._marked):
            for col_idx, value in enumerate(row):
                if value != 'X':
                    unmarked += int(self._board[row_idx][col_idx])

        return unmarked



def get_draws(data):
    return data[0].split(',')


def get_boards(data) -> List[Board]:
    boards:List[Board] = []
    start_idx = 2
    stop_idx = start_idx + BOARD_SIZE

    while start_idx<len(data):
        board = Board(data[start_idx:stop_idx])
        # print(board)
        boards.append(board)
        start_idx = stop_idx + 1
        stop_idx = start_idx + BOARD_SIZE

    return boards


def calculate(draws:List[str], boards:List[Board]):
    for draw in draws:
        for board in boards:
            if board.check(draw):
                unmarked = board.get_sum_unmarked()
                res = unmarked * int(draw)
                print(f'unmarked={unmarked}, draw={draw}')
                return res

def main():
    print('Part1:')
    draws = get_draws(INPUT.splitlines())
    print(draws)
    boards = get_boards(INPUT.splitlines())
    #print(boards)
    res = calculate(draws, boards)
    print(res)
    assert res == 4512

    data = util.read_data('day4.txt')
    draws = get_draws(data)
    print(draws)
    boards = get_boards(data)
    #print(boards)
    res = calculate(draws, boards)
    print(res)
    assert res == 51034


if __name__ == '__main__':
    main()
