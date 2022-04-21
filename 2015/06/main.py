from pickletools import uint8
import re
import numpy as np

f = open('input.txt', 'r')
instructions = f.read()
f.close()


lights = np.zeros((1000, 1000), int)
instructions = instructions.split('\n')


def turnOn(start, stop):
    # print('turnOn: ', int(start[0]), '-', stop[0], ', ', start[1], '-', stop[1])
    for i in range(int(start[0]), int(stop[0]) + 1):
        for j in range(int(start[1]), int(stop[1]) + 1):
            lights[i][j] += 1


def turnOff(start, stop):
    # print('turnOff: ', start[0], '-', stop[0], ', ', start[1], '-', stop[1])
    for i in range(int(start[0]), int(stop[0]) + 1):
        for j in range(int(start[1]), int(stop[1]) + 1):
            if lights[i][j] > 0: 
                lights[i][j] -= 1

def toggle(start, stop):
    # print('toggle: ', start[0], '-', stop[0], ', ', start[1], '-', stop[1])
    for i in range(int(start[0]), int(stop[0]) + 1):
        for j in range(int(start[1]), int(stop[1]) + 1):
            lights[i][j] += 2

count = 0 
for i in instructions:
    i = i.split(' ')
    # print(i)
    if i[0] == 'turn':
        if i[1] == 'on':
            turnOn(i[2].split(','), i[4].split(','))
        elif i[1] == 'off':
            turnOff(i[2].split(','), i[4].split(','))
    elif i[0] == 'toggle':
        toggle(i[1].split(','), i[3].split(','))
    
    # if count == 5:
    #     exit()
    count += 1



# print(np.count_nonzero(lights == True))

print(np.sum(lights))





