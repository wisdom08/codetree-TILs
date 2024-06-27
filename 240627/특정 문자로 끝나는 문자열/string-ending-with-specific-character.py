arr = [input() for _ in range(10)]
target = input()

for a in arr:
    if a[-1] == target:
        print(a)