import sys
input = sys.stdin.readline

a = input().rstrip()
a = list(a)
rev_a = a[::-1]

t = input().rstrip()
p1, p2 = 0, len(t) - 1
s1, s2 = [], [] 
len_a = len(a)

while p1 <= p2:
    while p1 <= p2:
        s1.append(t[p1])
        p1 += 1
        if s1[-len_a:] == a:
            s1[-len_a:] = []
            break
    while p1 <= p2:
        s2.append(t[p2])
        p2 -= 1
        if s2[-len_a:] == rev_a:
            s2[-len_a:] = []
            break

while s2:
    s1.append(s2.pop())
    if s1[-len_a:] == a:
        s1[-len_a:] = []
print(''.join(s1))
