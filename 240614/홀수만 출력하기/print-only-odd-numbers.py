n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


for i in arr:
    if i % 2 == 1 and i % 3 == 0:
        print(i)