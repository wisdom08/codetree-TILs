a, b = input().split()

al = len(a)
bl = len(b)
if al > bl:
    print(a, al)
elif al < bl:
    print(b, bl)
else:
    print('same')