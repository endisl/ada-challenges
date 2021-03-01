import sys
import re

nums = []  # creating an empty list

num = sys.stdin.readline()  # reading the first line of the input

while num != ''
 num = num.strip()  # removing white spaces
  res = re.match("[-+]?\d+$", num)  # checking if the number is an integer
   if (res is not None) and (0 < int(num) <= 20000):  # checking the restrictions
        num = int(num)
        nums.append(num)
        num = sys.stdin.readline()  # reading the next line of the input
    else:
        exit()

tot = nums[0]  # number of the elements of the set
serie = nums[1:]  # the elements of the set

if (tot == len(serie)) and (0 <= tot <= 2000):  # checking the restrictions
    print(max(serie) - min(serie))  # calculating the greatest difference
else:
    print(0)
