arr = list(map(int, input().split()))
print(arr[1] if arr[0] < arr[1] else arr[0])