


input = 3113322113
# input = 1123111


def look_and_say(input):
    output = ''
    lastChar = ' '
    count = 0
    for i in range(len(input)):
        # print('i: ', i, 'lastChar: ', lastChar, 'input[i]: ', input[i], 'count: ', count)
        if i == 0:
            lastChar = input[i]
        
        # if i == len(input) - 1:
        #     if lastChar == input[i]:
        #         count += 1
        #     else:
        #         count = 1
        #     output += str(count) + input[i]
        #     continue

        if lastChar == input[i]:
            count += 1
            if i == len(input) - 1:
                # count = 1
                # lastChar = input[i]
                output += str(count) + lastChar
            
            # continue
        
        else:
            output += str(count) + lastChar
            count = 1
            lastChar = input[i]
            if i == len(input) - 1:
                output += str(count) + lastChar
        # else:

            
        # print(input[i], end='\n\n')

    return output

result = '1'
i = 0
while(i < 70):
    # print(result)
    input = result
    result = look_and_say(input)
    print(len(result)/len(input))
    i += 1

# print('len of result is: ', len(result))