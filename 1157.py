n = input().upper()
a = [0 for i in range(26)]
for i in n:
    for j in range(26):
        if chr(65 + j) == i:
            a[j] += 1
b = sorted(a, reverse=True)
if b[0] == b[1]:
    print('?')
else:
    for i in range(26):
        if b[0] == a[i]:
            c = i
            print(chr(c + 65))
