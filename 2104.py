input = __import__('sys').stdin.readline

def solve(start, end):
    if start == end:
        return a[start] * a[start]

    mid = (start + end) // 2
    ans = max(solve(start, mid), solve(mid + 1, end))

    left, right = mid, mid + 1
    curSum = a[left] + a[right]
    minVal = min(a[left], a[right])
    ans = max(ans, curSum * minVal)

    while left > start or right < end:
        if right < end and (left == start or a[left - 1] < a[right + 1]):
            right += 1
            curSum += a[right]
            minVal = min(minVal, a[right])
        else:
            left -= 1
            curSum += a[left]
            minVal = min(minVal, a[left])
        ans = max(ans, curSum * minVal)
        
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(0, n-1))
