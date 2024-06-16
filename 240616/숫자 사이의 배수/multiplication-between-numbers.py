import math

a, b = map(int, input().split())

sum = 0
av = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        cnt += 1
        sum += i 
    

print(sum, round(sum / cnt, 1))