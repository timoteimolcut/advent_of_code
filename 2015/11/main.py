

def passIsValid(password):
    pass

def incrementPass(password):
    result = password
    l = len(result)
    if result[l-1] != 'z':
        print(1)
        result = result[0:l-1] + chr(ord(result[l-1]) + 1)
    elif result[l-2] != 'z':
        print(2)
        result = result[0:l-2] + chr(ord(result[l-2]) + 1) + 'a'
    elif result[l-3] != 'z':
        print(3)
        result = result[0:l-3] + chr(ord(result[l-3]) + 1) + 'aa'
    elif result[l-4] != 'z':
        print(4)
        result = result[0:l-4] + chr(ord(result[l-4]) + 1) + 'aaa'
    elif result[l-5] != 'z':
        print(5)
        result = result[0:l-5] + chr(ord(result[l-5]) + 1) + 'aaaa'
    elif result[l-6] != 'z':
        print(6)
        result = result[0:l-6] + chr(ord(result[l-6]) + 1) + 'aaaaa'
    elif result[l-7] != 'z':
        print(7)
        result = result[0:l-7] + chr(ord(result[l-7]) + 1) + 'aaaaaa'
    else:
        print(8)
        result = chr(ord(result[l-8]) + 1) + 'aaaaaaa'
    return result


word_list = ['a', 'a', 'a']

"""
0  - a >>> ord('a')=97
1  - b
2  - c
3  - d
4  - e
.
.
.
25 - z >>> ord('z')=122


Z modulo 26

"""


def word_to_list(word):
    list = []
    for c in word:
        # print(c, ord(c), ord(c) - ord('a'))
        list.append(ord(c) - ord('a'))
    # print(list)
    return list


def list_to_word(list):
    word = ''
    for el in list:
        word += chr(el + ord('a'))
    print(word)
    return word


def increment_word_list(list):
    # for i in range(len(list)):
    #     print(list[i])
    transport = 0
    if list[len(list)-1] == 25:
        transport = 1
    list[len(list)-1] = (list[len(list)-1] + 1) % 26
    for i in range(len(list)-2, -1, -1):
        if transport:
            list[i] = (list[i] + 1) % 26
            if list[i] == 0:
                transport = 1
            else:
                transport = 0
        else:
            if list[i] == 25:
                transport = 1
            else:
                transport = 0
        
    # print(list)
    return list

def main():
    # input = 'vzbxkghb'
    input = 'aaa'

    list = word_to_list(input)
    
    for i in range(17576):
        list_to_word(list)
        list = increment_word_list(list)
        

    # for i in range(208827064576):
    #     for c in input:
    #         print(c, end=' ')
    #     print()
    #     result = incrementPass(input)
    #     # print(result)
    #     input = result







if __name__ == '__main__':
    main()



