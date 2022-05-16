import sys
input = sys.stdin.readline

def binary(target, array, start, end):
    if start > end: return 0

    middle = (start + end) // 2
    if target == array[middle]:
        return 1
    elif target < array[middle]:
        return binary(target, array, start, middle - 1)
    else:
        return binary(target, array, middle + 1, end)

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = map(int, input().split())

for i in b:
    start = 0
    end = len(a) - 1
    print(binary(i, a, start, end))
