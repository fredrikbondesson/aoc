import util
from typing import List


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

        self._done = False

    def __str__(self) -> str:
        res = ''
        for row in self._board:
            res += str(row) + "\n"
        return res

    def check(self, nr: int):
        for row_idx, row in enumerate(self._board):
            for col_idx, value in enumerate(row):
                if nr == value:
                    # print(f'found {nr} in {row_idx} {col_idx}')
                    self._marked[row_idx][col_idx] = 'X'

        if self._check():
            return True

    def _check_row(self, row):
        if len([x for x in row if x=='X']) == BOARD_SIZE:
            self._done = True
            return True

    def check_column(self, col_idx):
        column = [self._marked[0][col_idx], self._marked[1][col_idx],
                self._marked[2][col_idx], self._marked[3][col_idx], self._marked[4][col_idx]]
        if len([x for x in column if x=='X']) == BOARD_SIZE:
            self._done = True
            return True

    def _check(self):
        for idx, row in enumerate(self._marked):
            if self._check_row(row) or self.check_column(idx):
                return True


    def get_sum_unmarked(self):
        sum = 0
        for row_idx, row in enumerate(self._marked):
            for col_idx, value in enumerate(row):
                if value != 'X':
                    #print(value)
                    sum += int(self._board[row_idx][col_idx])

        return sum


def get_draws(data):
    return data[0].split(',')


def get_boards(data) -> List[Board]:
    boards:List[Board] = []
    start_idx = 2
    stop_idx = start_idx + BOARD_SIZE

    while start_idx<len(data):
        board = Board(data[start_idx:stop_idx])
        #print(board)
        boards.append(board)
        start_idx = stop_idx + 1
        stop_idx = start_idx + BOARD_SIZE

    return boards


def calculate(draws:List[str], boards:List[Board]):
    all_result = []
    for draw in draws:
        for board in boards:
            if not board._done and board.check(draw):
                unmarked = board.get_sum_unmarked()
                res = unmarked * int(draw)
                # print(f'unmarked={unmarked}, draw={draw} res={res}')
                # Add assert for last one
                # unmarked=286, draw=19 res=5434
                all_result.append(res)
    return all_result


if __name__ == '__main__':
    print('Part1:')
    draws = get_draws(INPUT.splitlines())
    print(draws)
    boards = get_boards(INPUT.splitlines())
    #print(boards)
    res = calculate(draws, boards)
    print(res[-1])
    assert res[-1] == 1924

    data = util.read_data('2021/day4.txt')
    draws = get_draws(data)
    print(draws)
    boards = get_boards(data)
    #print(boards)
    res = calculate(draws, boards)
    print(res[-1])
    assert res[-1] == 5434

