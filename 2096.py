import sys
input = sys.stdin.readline

n = int(input())
maxs = [[0 for _ in range(3)] for _ in range(2)]
mins = [[0 for _ in range(3)] for _ in range(2)]

for i in range(n):
    temp = list(map(int, input().split()))
 
    maxs[1][0] = max(maxs[0][0], maxs[0][1]) + temp[0]
    mins[1][0] = min(mins[0][0], mins[0][1]) + temp[0]
 
    maxs[1][1] = max(maxs[0][0], maxs[0][1], maxs[0][2]) + temp[1]
    mins[1][1] = min(mins[0][0], mins[0][1], mins[0][2]) + temp[1]
 
    maxs[1][2] = max(maxs[0][1], maxs[0][2]) + temp[2]
    mins[1][2] = min(mins[0][1], mins[0][2]) + temp[2]
 
    maxs[0][0], maxs[0][1], maxs[0][2] = maxs[1][0], maxs[1][1], maxs[1][2]
    mins[0][0], mins[0][1], mins[0][2] = mins[1][0], mins[1][1], mins[1][2]

print(max(maxs[1]), min(mins[1]))
