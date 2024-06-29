s = input()

res = []
count = 1
for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        count += 1
        if i == len(s)-2:
            res.append(s[i])
            res.append(str(count))
    else:
        res.append(s[i])
        res.append(str(count))
        count = 1
    

print(len(res))
print(''.join(res))