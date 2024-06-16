a, b = map(int, input().split())

sum = 0

min, max = 0, 0

if a > b:
    max = a
    min = b
else:
    max = b
    min = a

for i in range(min, max+1):
    

    if i % 5 == 0:
        sum += i

print(sum)