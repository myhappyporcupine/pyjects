import random

rolls = []

def do_help():
    print('Available commands: help roll average exit')

def do_roll():
    rolled = random.randint(1, 6)
    print('You rolled', rolled)
    rolls.append(rolled)

def do_average():
    try:
        sum_of_rolls = 0
        for roll in rolls:
            sum_of_rolls += roll
        average = sum_of_rolls / len(rolls)
        print('You have rolled an overall average of', average)  
    except ZeroDivisionError:
        print('Error: you have not rolled anything yet')

while True:
    try:
        command = input('(dice) ')
        
        if command == 'help':
            do_help()
            
        elif command == 'roll':
            do_roll()
            
        elif command == 'average':
            do_average()
            
        elif command == 'exit':
            break
        
        else:
            print('Error: unknown command. type "help" for available commands.')

        print()
            
    except KeyboardInterrupt:
        break
