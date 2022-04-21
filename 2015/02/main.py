



f = open("input.txt", "r")
text = f.read()

# print(text)
operations = text.split()
totalArea = 0
totalRibbon = 0
for op in operations:
    nums = op.split('x')
    area1 = int(nums[0])*int(nums[1])
    area2 = int(nums[0])*int(nums[2])
    area3 = int(nums[1])*int(nums[2])
    p1 = 2 * (int(nums[0]) + int(nums[1]))
    p2 = 2 * (int(nums[0]) + int(nums[2]))
    p3 = 2 * (int(nums[1]) + int(nums[2]))
    totalArea += 2*(area1 + area2 + area3) + min(area1, area2, area3)
    totalRibbon += min(p1, p2, p3) + int(nums[0]) * int(nums[1]) * int(nums[2])
    
print('total area: ', totalArea)
print('total ribbon: ', totalRibbon)
f.close()



