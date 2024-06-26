n = int(input())

tl = 0
ac = 0

arr = [input() for _ in range(n)]

for i in arr:
    tl += len(i)
    for j in i:
        if j == 'a':
            ac += 1

print(tl, ac)