i = input()
arr = i.split()
a = int(arr[0])
b = int(arr[1])

answer = (10000 * b) // (a * a)
print(answer)

if(answer >= 25):
    print("Obesity")