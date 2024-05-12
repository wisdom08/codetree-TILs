arr = list(map(int, input().split()))

a = arr[0]
b = arr[1]

a += arr[1]
b += a 

print(a, b)