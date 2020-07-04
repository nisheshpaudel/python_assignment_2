value1 = int(input('Enter the first number: '))
value2 = int(input('Enter the second number: '))
operator = input('Enter operator (+, -, *, /): ')


def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return 'Perfectly divisible'
        return a / b
    else:
        return 'Unknown Operator'


print(calculator(value1, value2, operator))