arr = list(map(int, input().split()))

a = arr[0]
b = arr[1]

if a < b:
    print(1, 0)
elif a == b:
    print(0, 1)