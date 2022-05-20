input = __import__('sys').stdin.readline

a, b = map(str, input().rstrip().split())

ans = 100
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1
    ans = min(ans, count)

print(ans)
