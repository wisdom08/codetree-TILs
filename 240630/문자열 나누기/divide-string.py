# n개 입력 받기
# 입력받은 거 다 붙이고, 5개 씩 쪼갠다.
n = int(input())
arr = input().split()

str = ''.join(arr)

for i in range(0, len(str), 5):
    print(str[i:i+5])