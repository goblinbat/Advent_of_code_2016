"""
Advent of code 2016 day 1 (done as a challenge 3/14/19)

start facing north
turn left or right (depending if direction is l or r)
go the number of blocks directed

how many blocks away is the destination?
"""

north = 0
east = 0
south = 0
west = 0

facing = 'n'

def turn_right(number):
    global north
    global east
    global south
    global west
    global facing

    if facing == 'n':
        facing = 'e'
        east += number
    elif facing == 'e':
        facing = 's'
        south += number
    elif facing == 's':
        facing = 'w'
        west += number
    elif facing == 'w':
        facing = 'n'
        north += number

def turn_left(number):
    global north
    global east
    global south
    global west
    global facing
    
    if facing == 'n':
        facing = 'w'
        west += number
    elif facing == 'e':
        facing = 'n'
        north += number
    elif facing == 's':
        facing = 'e'
        east += number
    elif facing == 'w':
        facing = 's'
        south += number




if __name__ == '__main__':
    text = open('directions.txt', 'r')
    instruct = text.read().split(', ')

    for direct in instruct:
        go = direct.lower()
        if 'r' in go:
            num = int(go.replace('r', ''))
            turn_right(num)
            
        elif 'l' in go:
            num = int(go.replace('l', ''))
            turn_left(num)
    
    n_s = north - south
    e_w = east - west
    if n_s >= 0:
        print (f'{n_s} blocks north')
    elif n_s < 0:
        n_s = abs(n_s)
        print(f'{n_s} blocks south')
    if e_w >= 0:
        print(f'{e_w} blocks east')
    elif e_w < 0:
        e_w = abs(e_w)
        print(f'{e_w} blocks west')
    distance = n_s + e_w
    print(f'the headquarters is {distance} blocks away')


    text.close()
