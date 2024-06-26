n = int(input())

tl = 0
ac = 0

arr = [input() for _ in range(n)]

for i in arr:
    tl += len(i)
    if i[0] == 'a':
        ac += 1



print(tl, ac)