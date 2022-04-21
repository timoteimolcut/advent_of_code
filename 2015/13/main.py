import sys
import re
import math

nr_perm = 0
# this is not working ok, need for improvement 
def permutation(removed, people, count, limit):
    global nr_perm
    if count == limit:
        return
    for p in people:
        removed.add(p)
        people1 = people - removed
        permutation(removed, people1, count + 1, limit)
        removed.remove(p)
        # we have a new permutation
        if count == limit-1:
            nr_perm += 1
            for r in removed:
                print(r, end=' ')
            for p in people:
                print(p, end=' ')
            print()

def permutation_init(people):
    removed = set()
    limit = len(people)
    permutation(removed, people, 0, limit)


# def compute_happiness(perm):
    

def main():
    global nr_perm
    regex_pattern = re.compile(r"([A-Za-z]*) (would) (lose|gain) ([0-9]*) (happiness units by sitting next to) ([A-Za-z]*).")
    lines = sys.stdin.readlines()
    social = {}
    people = set()
    for l in lines:
        result = regex_pattern.search(l.strip())
        
        people.add(result.group(1))
        social[(result.group(1), result.group(6))] = int(result.group(4))
        if result.group(3) == 'lose':
            social[(result.group(1), result.group(6))] *= -1
        
    print(f'There are {len(people)} people.')

    # for k, v in social.items():
    #     print(k, v)
    

    # permutation_init(people)
    

    # part 1

    # listOfHappiness = []

    # for p0 in people:
    #     people1 = people.copy()
    #     people1.remove(p0)
    #     for p1 in people1:
    #         people2 = people1.copy()
    #         people2.remove(p1)
    #         for p2 in people2:
    #             people3 = people2.copy()
    #             people3.remove(p2)
    #             for p3 in people3:
    #                 people4 = people3.copy()
    #                 people4.remove(p3)
    #                 for p4 in people4:
    #                     people5 = people4.copy()
    #                     people5.remove(p4)
    #                     for p5 in people5:
    #                         people6 = people5.copy()
    #                         people6.remove(p5)
    #                         for p6 in people6:
    #                             people7=people6.copy()
    #                             people7.remove(p6)
    #                             for p7 in people7:
    #                                 nr_perm += 1
    #                                 perm = [p0, p1, p2, p3, p4, p5, p6, p7]
    #                                 print(perm)
    #                                 # happiness = social[(perm[0], perm[-1])] + social[(perm[-1], perm[0])]
    #                                 happiness = 0
    #                                 for i in range(-1, len(perm)-1):
    #                                     print(perm[i], perm[i+1])
    #                                     happiness += (social[(perm[i], perm[i+1])] + social[(perm[i+1], perm[i])])
    #                                     listOfHappiness.append(happiness)

    # print(nr_perm, math.factorial(len(people)))
    # print('result is: ', max(listOfHappiness))


    # part 2
    for p in people:
        social[('Tim', p)] = 0
        social[(p, 'Tim')] = 0
    
    people.add('Tim')

    listOfHappiness = []

    for p0 in people:
        people1 = people.copy()
        people1.remove(p0)
        for p1 in people1:
            people2 = people1.copy()
            people2.remove(p1)
            for p2 in people2:
                people3 = people2.copy()
                people3.remove(p2)
                for p3 in people3:
                    people4 = people3.copy()
                    people4.remove(p3)
                    for p4 in people4:
                        people5 = people4.copy()
                        people5.remove(p4)
                        for p5 in people5:
                            people6 = people5.copy()
                            people6.remove(p5)
                            for p6 in people6:
                                people7=people6.copy()
                                people7.remove(p6)
                                for p7 in people7:
                                    people8=people7.copy()
                                    people8.remove(p7)
                                    for p8 in people8:
                                        nr_perm += 1
                                        perm = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
                                        print(perm)
                                        # happiness = social[(perm[0], perm[-1])] + social[(perm[-1], perm[0])]
                                        happiness = 0
                                        for i in range(-1, len(perm)-1):
                                            # print(perm[i], perm[i+1])
                                            happiness += (social[(perm[i], perm[i+1])] + social[(perm[i+1], perm[i])])
                                            listOfHappiness.append(happiness)
    
    print(nr_perm, math.factorial(len(people)))
    print('result is: ', max(listOfHappiness))
        

if __name__ == '__main__':
    main()