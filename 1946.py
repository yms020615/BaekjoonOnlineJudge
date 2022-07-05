input = __import__('sys').stdin.readline

for _ in range(int(input())):
    n = int(input())
    grade = [list(map(int, input().split())) for _ in range(n)]

    grade.sort()
    count = 0
    maxGrade = grade[0][1]

    for i in grade[1:]:
        if i[1] > maxGrade:
            count += 1
        else:
            maxGrade = i[1]

    print(n - count)
