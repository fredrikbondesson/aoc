import util

SCORE_ILLEGAL = {')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }

SCORE_COMPLETING = {')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    }

INPUT="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


CLOSING = [')', ']', '}', '>']


def get_score_for_row(row):
    next_closing = []
    score = 0
    for idx, char in enumerate(row):
        if char in CLOSING:
            if char != next_closing[-1]:
                #print(row)
                #print(f'Incorrect ending was {char} but expected {next_closing[-1]} at position {idx}')

                score += SCORE_ILLEGAL[char]
                #print(f'{SCORE_ILLEGAL[char]} score={score}')
                return score, 0
            else:
                # print(f'Incomplete row={row}')
                next_closing.pop()

        if char == '(':
            next_closing.append(')')
        elif char == '[':
            next_closing.append(']')
        elif char == '{':
            next_closing.append('}')
        elif char == '<':
            next_closing.append('>')

    print(f'Incomplete row={row}')
    print(next_closing)

    closing_score = get_closing_score(next_closing)
    print(f'Closing score={closing_score}')
    return score, closing_score


def get_closing_score(closings):
    score = 0
    try:
        closing = closings.pop()
        while closing:
            score = 5 * score + SCORE_COMPLETING[closing]
            closing = closings.pop()
    except IndexError:
        pass

    return score


def main():
    score = 0
    closing_scores = []
    for row in INPUT.split('\n'):
        print(row)
        illegal_score, closing_score = get_score_for_row(row)
        print(illegal_score, closing_score)
        if closing_score != 0:
            closing_scores.append(closing_score)
        score += illegal_score

    print(f'Score={score}')
    assert score == 26397

    print(f'closing_scores={closing_scores}')

    print(sorted(closing_scores))
    print(sorted(closing_scores)[int(len(closing_scores)/2)])

    assert sorted(closing_scores)[int(len(closing_scores)/2)] == 288957

    closing_scores = []
    rows = util.read_data('2021/day10.txt')
    score = 0
    for row in rows:
        illegal_score, closing_score = get_score_for_row(row)
        if closing_score != 0:
            closing_scores.append(closing_score)
        score += illegal_score

    print(f'Score={score}')
    assert score == 311895

    print(f'closing_scores={closing_scores}')

    print(sorted(closing_scores))
    print(sorted(closing_scores)[int(len(closing_scores)/2)])

    assert sorted(closing_scores)[int(len(closing_scores)/2)] == 2904180541


if __name__ == '__main__':
    main()
