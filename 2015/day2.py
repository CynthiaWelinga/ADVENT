"""
Fortunately, every present is a box (a perfect right rectangular prism), 
which makes calculating the required wrapping paper for each gift a little easier: 
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 

The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper 
plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper 
plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""


import requests


file_path = 'C:/Users/CynthiaWelinga/DEVELOPMENT/ADVENT/2015/day2.txt'
puzzle_input = open(file_path).readlines()
dimensions = []
total = 0


for i in puzzle_input:
    dimensions.append(i.strip())

for item in dimensions:
    item = sorted(item.split('x'))
    for num in item:
        nums =[int(num) for num in item]
    nums.sort()


    total += (2*(nums[0]*nums[1]) + 2*(nums[1]*nums[2]) + 2*(nums[2]*nums[0])) + (nums[0]*nums[1])

    
print(total)



"""
The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
"""