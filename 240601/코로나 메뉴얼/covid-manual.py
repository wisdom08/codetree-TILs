arr = []
cnt = 0
for _ in range(3):
    temp = list(input().split())
    if temp[0] == 'Y' and int(temp[1]) >= 37:
        cnt += 1
    

if cnt >= 2:
    print("E")
else:
    print("N")