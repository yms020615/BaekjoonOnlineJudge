import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
s = list(map(int, input().split()))

if k >= n:
    print(0)
    exit(0)

s.sort()
diff = [s[i] - s[i-1] for i in range(1, n)]
diff.sort()
print(sum(diff[:n-k]))
