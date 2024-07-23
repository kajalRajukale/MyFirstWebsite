import random
height = 15
def christmas_tree():
    print('\n')
    for i in range(height):
        print(' ' * (height - i), end='')
        for j in range((2 * i) + 1):
            if random.random() < 0.1:
                color = random.choice(['\033[1;31m', '\033[33m', '\033[1;34m'])
                print(color, end='')  #  the lights 
            else:
                print('\033[32m', end='')  #  green 
            print('*', end='')
        print()
    print((' ' * height) + '|')
    print((' ' * 8) + 'Merry Christmas! To you')
    print((' ' * 13) + '2024\n')

christmas_tree()