input = __import__('sys').stdin.readline

n, m = map(int, input().split())
s = [input().rstrip() for _ in range(n)]
for i in s:
    print(i[::-1])
