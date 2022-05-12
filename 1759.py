from itertools import combinations

l, c = map(int, input().split())
s = list(map(str, input().split()))
s.sort()
com = combinations(s, l)
vow = 'aeiou'
cons = 'bcdfghjklmnpqrstvwxyz'
for i in com:
    tmp1, tmp2, tmp3 = False, False, False
    for j in vow:
        if j in i:
            tmp1 = True
            break
    for j in cons:
        if j in i:
            if not tmp2:
                tmp2 = True
            else:
                tmp3 = True
                break
    if False in (tmp1, tmp2, tmp3):
        continue
    print(''.join(i))
