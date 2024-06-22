arr = [input() for _ in range(3)]

max = len(arr[0])
min = len(arr[0])

for i in range(1, 3):
    n = len(arr[i])
    if max < n:
        max = n
    elif min > n:
        min = n

print(max-min)