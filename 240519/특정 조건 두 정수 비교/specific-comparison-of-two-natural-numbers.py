arr = list(map(int, input().split()))

a = arr[0]
b = arr[1]

if a < b:
    print(1, end=" ")
else:
    print(0, end=" ")


if a == b:
    print(1)
else:
    print(0)