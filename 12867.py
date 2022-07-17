input = __import__('sys').stdin.readline

n = int(input())
m = int(input())
s = list(map(int, input().split()))
move = input().rstrip()

d = {}
for i in s:
    d[i] = 0

l = []
l.append([0] * len(d))
for i in range(m):
    if move[i] == '+':
        d[s[i]] += 1
    elif move[i] == '-':
        d[s[i]] -= 1
    
    l.append(list(d.values()))

l.sort()
for i in range(len(l) - 1):
    if l[i] == l[i+1]:
        print(0)
        exit(0)
print(1)
