input = __import__('sys').stdin.readline
__import__('sys').setrecursionlimit(500000)

def merge_sort(start, end):
    global count

    if start < end:
        mid = (start + end) >> 1
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        x, y = start, mid + 1
        temp = []

        while x <= mid and y <= end:
            if a[x] <= a[y]:
                temp.append(a[x])
                x += 1
            else:
                temp.append(a[y])
                y += 1
                count += (mid - x + 1)
            
        if x <= mid:
            temp = temp + a[x:mid + 1]
        if y <= end:
            temp = temp + a[y:end + 1]

        for i in range(len(temp)):
            a[start + i] = temp[i]


n = int(input())
a = list(map(int, input().split()))
count = 0
merge_sort(0, n-1)
print(count)
