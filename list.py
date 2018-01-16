the_list = ['first thing']

def print_list():
    print('The list now contains:')
    for thing in the_list:
        print(thing)
    print()

print_list()
while True:
    try:
        new_thing = input('Append to the list (or press Ctrl-C to exit): ')
        the_list.append(new_thing)
        print_list()
    except KeyboardInterrupt:
        break
