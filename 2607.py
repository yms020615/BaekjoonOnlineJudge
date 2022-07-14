import sys
input = sys.stdin.readline

def check(first, word):
    a = [0 for _ in range(26)]
    b = [0 for _ in range(26)]

    for i in first:
        a[ord(i) - ord('A')] += 1
    for i in word:
        b[ord(i) - ord('A')] += 1

    diff = 0
    for i in range(26):
        if a[i] != b[i]:
            diff += abs(a[i] - b[i])

    if len(first) == len(word):
        return 1 if diff < 3 else 0
    else:
        return 1 if diff < 2 else 0

n = int(input())
first = list(map(str, input().rstrip()))
words = [list(map(str, input().rstrip())) for _ in range(n - 1)]

ans = 0
for i in words:
    ans += check(first, i)
print(ans)
