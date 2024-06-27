s = input()
n = int(input())
l = len(s)

if l < n:
    for i in range(l):
        print(s[l-i-1], end="")
else:
    for i in range(n):
        print(s[l-i-1], end="")