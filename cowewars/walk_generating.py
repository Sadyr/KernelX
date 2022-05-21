
def is_valid_walk(directions):
    point = 0
    count = 0

    for dir in directions:
        if dir == 'n':
            point = point + 1
        if dir == 's':
            point = point - 1
        if dir == 'w':
            point = point + 1
        if dir == 'w':
            point = point - 1
        count = count + 1
    print(point)
    print(count)
    if point == 0 and count == 10:
        return True
directions =    ['e', 'w', 'w', 's', 'e', 'e', 'e', 'n']
is_valid_walk(directions)


