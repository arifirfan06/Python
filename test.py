picture = [[0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0]]

for img in picture:
    for item in img:
        if (item == 0):
            print(' ', end='')
        if (item == 1):
            print('*', end='')
    print('')
