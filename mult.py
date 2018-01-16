import random

print('Multiplication table practice (press Ctrl-C to exit)')

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    try:
        answer = int(input(str(a) + ' X ' + str(b) + ' = '))
        if answer == a * b:
            print(':)')
        else:
            print(':(')
    except ValueError:
        print('Error: not an integer')
    except KeyboardInterrupt:
        print('Bye!')
        break
