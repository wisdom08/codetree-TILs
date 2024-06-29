res = ''
str = input()
for i in range(1, len(str), 2):
    res += str[i]

print(res[::-1])