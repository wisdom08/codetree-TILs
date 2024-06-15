arr = [int(input()) for _ in range(10)]

cnt = 0

for n in arr:
    if n % 2 == 1:
        cnt += 1

print(cnt)