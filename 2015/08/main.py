import sys

lines = sys.stdin.readlines()

#part one
countChars = 0


for line in lines:
    code = line.strip()
    print(code)
    print('code len: ', len(code))
    counter = 0

    i = 1
    while i < len(code) - 1:
        # print(i, code[i], hex(ord(code[i])))

        if hex(ord(code[i])) == '0x5c':
            if hex(ord(code[i+1])) == '0x5c':
                counter += 1
                i+=2
                print('ok1')
                continue
            elif hex(ord(code[i+1])) == '0x22':
                counter += 1
                i+=2
                print('ok2')
                continue
            elif hex(ord(code[i+1])) == '0x78':
                counter += 1
                i+=4
                print('ok3')
                continue
        counter += 1
        i += 1
    print('memory size: ', counter)
    countChars += len(code) - counter


print('result is: ', countChars)


# part two
countChars = 0

for line in lines:
    code = line.strip()
    print(code)
    print('code len: ', len(code))
    
    counter = 0
    i = 0
    while i < len(code):
        # print(i, code[i], hex(ord(code[i])))

        if hex(ord(code[i])) == '0x5c':
            counter += 2
            i += 1
            continue
        elif hex(ord(code[i])) == '0x22':
            counter += 2
            i += 1
            continue
        counter += 1
        i += 1
        
    counter += 2
    print('memory size: ', counter)
    countChars += counter - len(code)

print('result is: ', countChars)





