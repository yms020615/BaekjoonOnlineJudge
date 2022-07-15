import sys
input = sys.stdin.readline

s = '123456789'
nums = set()

for i in s:
    for j in s:
        for k in s:
            for l in s:
                nums.add(min(int(i + j + k + l), int(j + k + l + i), int(k + l + i + j), int(l + i + j + k)))

nums = sorted(nums)
i, j, k, l = map(str, input().rstrip().split())
n = min(int(i + j + k + l), int(j + k + l + i), int(k + l + i + j), int(l + i + j + k))
print(nums.index(n) + 1)
