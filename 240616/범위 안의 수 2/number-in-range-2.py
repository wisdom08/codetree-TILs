import math 

nums = [int(input()) for _ in range(10)]

sum, av, cnt = 0, 0, 0

for i in nums:
    if i >= 0 and i <= 200:
        sum += i
        cnt += 1


print(sum, round(sum / cnt, 1))