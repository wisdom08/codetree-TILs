n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or str(i).find('3') != -1 or str(i).find('6') != -1 or str(i).find('9') != -1:
        print(0, end=" ")
    else:
        print(i, end=" ")