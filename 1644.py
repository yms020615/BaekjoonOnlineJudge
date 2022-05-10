n = int(input())

erat = [True] * (n+1)
erat[0], erat[1] = False, False
def eratos():
    for i in range(2, int(n ** 0.5) + 1):
        if erat[i]:
            for j in range(2*i, n+1, i):
                erat[j] = False
    return [i for i in range(2, n+1) if erat[i] == True]

s = eratos()
ans = 0
start = 0
end = 0
while end <= len(s):
    temp_sum = sum(s[start:end])
    if temp_sum == n:
        ans += 1
        end += 1
    elif temp_sum < n:
        end += 1
    else:
        start += 1

print(ans)
