arr = ["apple", "banana", "grape", "blueberry", "orange"]

s = input()
cnt = 0

for i in range(5):
    if arr[i][2] == s or arr[i][3] == s:
        cnt += 1
        print(arr[i])

print(cnt)