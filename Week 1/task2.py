""" Калькулятор с предвидением ошибок """
A = float(input())
B = float(input())
SIM = str(input())
try:
    if SIM == '+':
        print(format(A+B, '.2f'))
    elif SIM == '-':
        print(format(A-B, '.2f'))
    elif SIM == '/':
        print(format(A/B, '.2f'))
    elif SIM == '*':
        print(format(A*B, '.2f'))
    else:
        print('ЫЫЫЫЫЫ')
except ZeroDivisionError:
    print('ЫЫЫЫЫЫ')
