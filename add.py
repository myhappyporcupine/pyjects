try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print('The sum of ' + str(a) + ' and ' + str(b) + ' is ' + str(a+b))
except ValueError:
    print('Error: not an integer number')
