input = __import__('sys').stdin.readline

from collections import defaultdict

for _ in range(int(input())):
    m = int(input())

    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    a, b = defaultdict(list), defaultdict(list)
    for i in left:
        a[i % 500].append(i // 500)
    for i in right:
        b[i % 500].append(i // 500)

    s = []
    for i in a:
        for j in range(len(a[i])):
            s.append((a[i][j], b[i][j]))

    ans = 0
    for i in s:
        if i[0] < i[1]:
            ans += 1

    print(ans // 2)
