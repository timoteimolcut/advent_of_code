import sys
import math

lines = sys.stdin.readlines()

destinations = set()
roads = {}

for line in lines:
    line = line.strip()
    cities, dist = line.split(' = ')
    a, b = cities.split(' to ')
    # print(a, b, dist)
    destinations.add(a)
    destinations.add(b)
    roads[(a, b)] = int(dist)
    roads[(b, a)] = int(dist)


# for k, v in roads.items():
#     print(k, v)

counter = 0
distances = []

for d in destinations:
    destinations1 = destinations.copy()
    destinations1.remove(d)

    for d1 in destinations1:
        destinations2 = destinations1.copy()
        destinations2.remove(d1)

        for d2 in destinations2:
            destinations3 = destinations2.copy()
            destinations3.remove(d2)

            for d3 in destinations3:
                destinations4 = destinations3.copy()
                destinations4.remove(d3)

                for d4 in destinations4:
                    destinations5 = destinations4.copy()
                    destinations5.remove(d4)

                    for d5 in destinations5:
                        destinations6 = destinations5.copy()
                        destinations6.remove(d5)

                        for d6 in destinations6:
                            destinations7 = destinations6.copy()
                            destinations7.remove(d6)

                            for d7 in destinations7:
                                # print(d)
                                
                                # print(d, d1, d2, d3, d4, d5, d6, d7, sum)
                                # print(roads[(d, d1)], roads[(d1, d2)], roads[(d2, d3)], roads[(d3, d4)], roads[(d4, d5)], roads[(d5, d6)], roads[(d6, d7)])
                                route = [roads[(d, d1)], roads[(d1, d2)], roads[(d2, d3)], roads[(d3, d4)], roads[(d4, d5)], roads[(d5, d6)], roads[(d6, d7)]]
                                distances.append(sum(route))
                                counter += 1
                                

print('minimum distance: ', min(distances))
# print(len(destinations), math.factorial(len(destinations)), counter)


# part two
print('maximum distance: ', max(distances))
