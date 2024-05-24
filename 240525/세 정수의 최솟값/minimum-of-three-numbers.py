arr = list(map(int, input().split()))

if arr[0] < arr[1] and arr[0] < arr[2]:
    print(arr[0])
elif arr[1] < arr[0] and arr[1] < arr[2]:
    print(arr[1])
else:
    print(arr[2])