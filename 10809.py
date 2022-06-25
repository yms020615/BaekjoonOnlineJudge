a = input()
b = [-1 for i in range(26)]
for i in range(ord('a'), ord('z') + 1):
    b[i - ord('a')] = a.find(chr(i))
    print(b[i - ord('a')], end = ' ')
