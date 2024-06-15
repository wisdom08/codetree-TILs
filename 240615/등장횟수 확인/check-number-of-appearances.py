nums = [int(input()) for _ in range(5)]

cnt = 0

for n in nums:
    if n % 2 == 0:
        cnt += 1

print(cnt)