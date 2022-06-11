p = []
for i in range(int(input())):
    p = list(map(int, input().split()))
    count = 0
    average = sum(p[1:]) / (len(p) - 1)
    for j in p[1:]:
        if j > average:
            count += 1
    print('%.3f%%' % (count / p[0] * 100))
