a = input()
b = input()
c = input()

al = len(a)
bl = len(b)
cl = len(c)

mx = max([al, bl, cl])
mi = min([al, bl, cl])

print(mx-mi)