import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [0] + [int(input()) for _ in range(n)]

    count = 1
    curr = a[1]
    while curr != n and count <= 10000:
        curr = a[curr]
        count += 1

    print(count if count <= 10000 else 0)
