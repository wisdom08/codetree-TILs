arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]
c = arr[2]

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)

elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)

elif c > a and c > b:
     if b > a:
        print(b)
     else:
        print(a)