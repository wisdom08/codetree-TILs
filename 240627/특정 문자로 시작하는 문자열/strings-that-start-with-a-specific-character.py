n = int(input())
arr = [input() for _ in range(n)]

target = input()

count = 0
av = 0

for a in arr:
    if a[0] == target:
        count += 1
        av += len(a)

print(count, f'{av/count:.2f}')