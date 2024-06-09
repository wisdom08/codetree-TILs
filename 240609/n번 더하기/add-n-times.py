a, n = map(int, input().split())

result = a
for _ in range(n):
    result += n
    print(result)