import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

ans = 0
while len(s) > 1:
    lowest, idx = 0, -1
    for i in range(len(s)):
        if lowest < s[i]:
            lowest = s[i]
            idx = i
    
    if idx == 0:
        ans += lowest - s[1]
        s.remove(lowest)

    elif idx == len(s) - 1:
        ans += lowest - s[-2]
        s.remove(lowest)
    
    else:
        ans += min(lowest - s[idx - 1], lowest - s[idx + 1])
        s.remove(lowest)

print(ans)
