n = int(input())
s = list(map(int, input().split()))

s.sort()
ans = 0
for i in range(1, n+1):
    ans += sum(s[:i])
    
print(ans)
