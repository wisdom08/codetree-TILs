a, b, c = 0, 0, 0
n = int(input())

# a: 2일마다 -> 2의 배수
# b: 3 -> 3의 배수
# c: 12 -> 12의 배수
# 겹치면 주기가 더 긴 거한다.
11 
for i in range(2, n+1):
    if i % 12 == 0:
        c += 1
    elif i % 3 == 0:
        b += 1
    elif i % 2 == 0:
        a += 1

print(a, b, c)