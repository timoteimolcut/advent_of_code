

import hashlib
  
input = 'iwrupvqb'
number = 1
while True:
    combine = input + str(number)
    # print('input: ', input)
    result = hashlib.md5(combine.encode())
    if result.hexdigest()[0:6] == '000000':
        break
    number += 1


print(f"hexadecimal value= {result.hexdigest()} number= {number}")




