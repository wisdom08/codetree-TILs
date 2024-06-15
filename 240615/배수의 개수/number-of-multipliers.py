nums = [int(input()) for _ in range(10)]

cnt3 = 0
cnt5 = 0

for n in nums:
    if n % 3 == 0:
        cnt3 += 1
    if n % 5 == 0:
        cnt5 += 1

print(cnt3, cnt5)