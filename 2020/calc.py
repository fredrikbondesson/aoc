from operator import pow, truediv, mul, add, sub

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}


operators2 = {
    '+': add,
    '-': sub,
    '*': mul,
#   '/': truediv
}


def calculate(expression):
    if expression.isdigit():
        return int(expression)
    for c in operators.keys():
        left, operator, right = expression.partition(c)
        print(c, left, operator, right)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))


def calculate2(expression):
    if expression.isdigit():
        return int(expression)
    for c in operators2.keys():
        left, operator, right = expression.partition(c)
        print(c, left, operator, right)
        if operator in operators2:
            return operators2[operator](calculate2(left), calculate2(right))


# calc = input("Type calculation:\n")
# print("Answer: " + str(calculate(calc)))

# print(calculate('1+2+4*3*1'))
# .replace(' ', '')
# print(calculate2('1+(2*3)+(4*(5+6))'))

INPUT = '1 + 2 * 3 + 4 * 5 + 6'.replace(' ', '')
print(calculate(INPUT))
print(calculate2(INPUT))
