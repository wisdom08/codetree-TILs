arr = list(map(int, input().split()))

if arr[0] >= 90:
    if arr[1] >= 95:
        print(100000)
    elif arr[1] >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)