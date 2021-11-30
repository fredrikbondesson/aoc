import util
from operator import mul, add, sub


operators = {
  '+': add,
  '-': sub,
  '*': mul,
  #'/': truediv
}


def evaluate(expression):
    print('evaluate ' + expression)
    # import pdb; pdb.set_trace()
    if expression.isdigit():
        print('evaluate returning here: ' + expression)
        return int(expression)
    #import pdb; pdb.set_trace()
    operator = None
    left_expression = None
    for idx, item in enumerate(expression):
        print(idx, item)
        if item == '+' or item == '-' or item == '*':
            operator = item

        elif item == '(':
            right_expression = evaluate(expression[idx + 1:])
            print(left_expression, right_expression)
            # import pdb; pdb.set_trace()
            sum = operators[operator](int(left_expression), right_expression)
            print('sum ', sum)
            return sum
        else:
            left_expression = item


            # if operator == '*':
            #     sum *= int(item)
            # elif operator == '+':
            #     sum += int(item)
            # elif operator == '-':
            #     sum -= int(item)
            # elif not operator:
            #     sum = int(item)

            # print(item, sum)
    print("AAAAAAAAAA")


def calc2(expression, exp_sum):

    print(expression)
    expression = expression.replace("(", "( ")
    expression = expression.replace(")", " )")

    print(expression)

    res = evaluate(expression)

    assert res == exp_sum


def calc(expression, exp_sum):
    print(expression)
    sum = 0
    operator = None
    for idx, item in enumerate(expression):
        if item == '+' or item == '-' or item == '*':
            operator = item
        elif item == ' ':
            pass
        else:
            if operator == '*':
                sum *= int(item)
            elif operator == '+':
                sum += int(item)
            elif operator == '-':
                sum -= int(item)
            elif not operator:
                sum = int(item)

            print(item, sum)

    assert sum == exp_sum


def main():
    INPUT = '1 + 2 * 3 + 4 * 5 + 6'
    # data = INPUT.split('\n')
    # INPUT.replace(' ', '')
    util.measure_time_for(calc, INPUT, 71)

    #INPUT = '1 + (2 * 3) + (4 * (5 + 6))'
    #util.measure_time_for(calc, INPUT, 51)

    util.measure_time_for(calc2, INPUT.replace(' ', ''), 71)


if __name__ == '__main__':
    main()
