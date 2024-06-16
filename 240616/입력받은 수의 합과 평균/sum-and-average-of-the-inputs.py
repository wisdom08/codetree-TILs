import math 

n = int(input())
nums = [int(input()) for _ in range(n)]

sum, av = 0, 0

for i in nums:
    sum += i

print(sum, round(sum/n, 1))