n = int(input())

arr = []

for i in range(1, n+1):
    if i % 2 == 0 or str(i)[-1] == '5' or (i % 3 == 0 and i % 9 != 0):
        continue
    
    arr.append(i)

print(*arr)