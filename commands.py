def do_help():
    print('Available commands: help one two three exit')

def do_one():
    print('Command one executed')

def do_two():
    print('Command two executed')

def do_three():
    print('Command three executed')

while True:    
    command = input('(prompt) ')

    if command == 'help':
        do_help()

    elif command == 'one':
        do_one()

    elif command == 'two':
        do_two()

    elif command == 'three':
        do_three()

    elif command == 'exit':
        break

    else:
        print('Unknown command')
