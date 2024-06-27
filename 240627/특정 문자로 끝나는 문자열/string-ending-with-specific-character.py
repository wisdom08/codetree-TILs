arr = [input() for _ in range(10)]
target = input()

count = 0
for a in arr:
    if a[-1] == target:
        count +=1 
        print(a)


if count == 0:
    print('None')