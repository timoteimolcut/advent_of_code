

vowels = 'aeiou'

def isNice(word):
    # print(word)

    #3 vowels
    no_vowels = 0
    for v in vowels:
        no_vowels += word.count(v)
    if no_vowels < 3:
        return False
    
    #double letters
    double = False
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            double = True
    if double == False:
        return False
    
    if ('ab' in word) or ('cd' in word) or ('pq' in word) or ('xy' in word):
        return False
    
    return True
    
#second one
def isNicer(word):
    ddouble = False
    # print(word)
    for i in range(len(word) - 1):
        # print(word[i:i+2])
        # print(word[0:i],' ', word[i+2:])
        
        if word[0:i].count(word[i:i+2]) + word[i+2:].count(word[i:i+2]) > 0:
            ddouble = True
            break
    # exit()
    if ddouble == False:
        return False
    double = False
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            double = True
            break
    if double == False:
        return False

    return True
    

f = open('input.txt', 'r')

text = f.read()
# print(text)
f.close()

count = 0
for w in text.split():
    if isNicer(w):
        count += 1

print('count: ', count)
