n = int(input())
cnt = 0

# 4로 나누었을 때 나머지 0
# 100으로 나웠을 때 나머지 0 and 400으로 나누어 떨어지지 않으면? 평년

for i in range(1, n+1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 !=0:
            continue
        else:
            cnt += 1
    
print(cnt)