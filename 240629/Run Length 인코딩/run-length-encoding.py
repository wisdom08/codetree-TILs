s = input()

encoded = ""

cur_char = s[0]
num_char = 1

for target in s[1:]:
    if target == cur_char:
        num_char += 1
    else:
        encoded += cur_char
        encoded += str(num_char)

        cur_char = target
        num_char = 1

encoded += cur_char
encoded += str(num_char)

print(len(encoded))
print(encoded)