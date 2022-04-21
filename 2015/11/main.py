import time



# def incrementPass(password):
#     result = password
#     l = len(result)
#     if result[l-1] != 'z':
#         print(1)
#         result = result[0:l-1] + chr(ord(result[l-1]) + 1)
#     elif result[l-2] != 'z':
#         print(2)
#         result = result[0:l-2] + chr(ord(result[l-2]) + 1) + 'a'
#     elif result[l-3] != 'z':
#         print(3)
#         result = result[0:l-3] + chr(ord(result[l-3]) + 1) + 'aa'
#     elif result[l-4] != 'z':
#         print(4)
#         result = result[0:l-4] + chr(ord(result[l-4]) + 1) + 'aaa'
#     elif result[l-5] != 'z':
#         print(5)
#         result = result[0:l-5] + chr(ord(result[l-5]) + 1) + 'aaaa'
#     elif result[l-6] != 'z':
#         print(6)
#         result = result[0:l-6] + chr(ord(result[l-6]) + 1) + 'aaaaa'
#     elif result[l-7] != 'z':
#         print(7)
#         result = result[0:l-7] + chr(ord(result[l-7]) + 1) + 'aaaaaa'
#     else:
#         print(8)
#         result = chr(ord(result[l-8]) + 1) + 'aaaaaaa'
#     return result
# word_list = ['a', 'a', 'a']

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
        list.append(ord(c) - ord('a'))
    return list


def list_to_word(list):
    word = ''
    for el in list:
        word += chr(el + ord('a'))
    return word


def increment_word_list(list):
    transport = 0
    if list[-1] == 25:
        transport = 1
    list[-1] = (list[-1] + 1) % 26
    for i in range(len(list)-2, -1, -1):
        list[i] = (list[i] + transport) % 26
        if transport == 1 and list[i] == 0:
            transport = 1
        else:
            transport = 0
    return list



groups = [chr(x + ord('a')) + chr(x + 1 + ord('a')) + chr(x + 2 + ord('a')) for x in range(24)]
pairs = [chr(x + ord('a')) + chr(x + ord('a')) for x in range(26)]


def passIsValid(password):
    print('passIsValid: ', password)
    # print(groups)
    # print(pairs)

    if ('i' in password) or ('o' in password) or ('l' in password):
        print(1)
        return False
    
    # abc, bcd, cde, and so on, up to xyz
    contains = False
    for g in groups:
        if g in password:
            contains = True
            break
    if contains == False:
        print(2)
        return False
    
    # like aa, bb, or zz
    count = 0
    for p in pairs:
        if p in password:
            count += 1
    if count < 2:
        print(3)
        return False

    print('ok')
    return True
    

def main():
    input = 'vzbxkghb'
    # part two
    input = 'vzbxxyzz'
    list = word_to_list(input)
    iterations = 26**len(input)

    start = time.time()    
    for i in range(iterations):
        # list_to_word(list) dureaza mai putin decat print(list)
        list = increment_word_list(list)
        if passIsValid(list_to_word(list)) == True:
            break
    print(f'total time:  {time.time() - start} seconds')
    print(f'The next password is: {list_to_word(list)}')
    
    

    # for i in range(iterations):
    #     result = incrementPass(input)
    #     print(result)
    #     input = result






if __name__ == '__main__':
    main()



