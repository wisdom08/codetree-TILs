i = input()
a = int(i.split(" ")[0])
b = int(i.split(" ")[1])
answer = (10000 * b) // (a * a)
print(answer)

if(answer >= 25):
    print("Obesity")