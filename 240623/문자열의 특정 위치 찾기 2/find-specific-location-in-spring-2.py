arr = ["apple", "banana", "grape", "blueberry", "orange"]

s = input()
cnt = 0

for i, e in enumerate(arr):
    for j in range(2, 4):
        if arr[i][j] == s:
            cnt += 1
            print(arr[i])
            break

print(cnt)