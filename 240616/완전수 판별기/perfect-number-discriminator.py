n = int(input())
# 약수 -> 나머지가 0

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("P")
else:
    print("N")