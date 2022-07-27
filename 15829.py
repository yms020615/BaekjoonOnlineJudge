import sys
input = sys.stdin.readline

n = int(input())
s = list(map(str, input().strip('\n')))
j = 0
hash = 0
for i in s:
    hash += (ord(i) - ord('a') + 1) * (31 ** j)
    j += 1
print(hash % 1234567891)
