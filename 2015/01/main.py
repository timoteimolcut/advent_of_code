



f = open("input.txt", "r")
text = f.read()

# print(text)

count = 0
for i in range(len(text)):
    print(i, count)
    if count == -1:
        # print(i+1)
        break
    if text[i] == '(':
        count += 1
    elif text[i] == ')':
        count -= 1

print('final count down: ', count)

f.close()



