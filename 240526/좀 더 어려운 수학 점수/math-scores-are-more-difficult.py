a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1. 수학 점수 높은 사람 
# 2. 수학 점수 같으면 영어 점수 높은 사람 

if a[0] > b[0]:
    print("A")
elif a[0] < b[0]:
    print("B")
elif a[1] > b[1]:
    print("A")
else:
    print("B")