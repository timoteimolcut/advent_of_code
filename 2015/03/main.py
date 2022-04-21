



f = open('input.txt', 'r')
theMap = f.read()
print(theMap)

countMoves = 1
pos1 = [0, 0]
pos2 = [0, 0]

houses1 = {tuple(pos1)}
houses2 = {tuple(pos2)}
for i in range(len(theMap)):
    # countMoves+=1
    # print(tuple(pos))

    
    if i % 2 == 0:
        if theMap[i] == '>':
            pos1[0] += 1
        elif theMap[i] == 'v':
            pos1[1] += 1
        elif theMap[i] == '<':
            pos1[0] -= 1
        elif theMap[i] == '^':
            pos1[1] -= 1
        houses1.add(tuple(pos1))
    else:
        if theMap[i] == '>':
            pos2[0] += 1
        elif theMap[i] == 'v':
            pos2[1] += 1
        elif theMap[i] == '<':
            pos2[0] -= 1
        elif theMap[i] == '^':
            pos2[1] -= 1
        houses2.add(tuple(pos2))


print(f'# houses1= {len(houses1)}, # houses2= {len(houses2)}, # union={len(houses1.union(houses2))}')



f.close()