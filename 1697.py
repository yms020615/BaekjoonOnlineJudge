input = __import__('sys').stdin.readline

from collections import deque

n, k = map(int, input().split())

def bfs(n):
    visited = [0 for _ in range(100001)]
    queue = deque([n])

    while queue:
        curr = queue.popleft()

        if curr == k:
            print(visited[curr])
            exit(0)

        if 0 <= curr - 1 <= 100000 and not visited[curr - 1]:
            visited[curr - 1] = visited[curr] + 1
            queue.append(curr - 1)
        if 0 <= curr + 1 <= 100000 and not visited[curr + 1]:
            visited[curr + 1] = visited[curr] + 1
            queue.append(curr + 1)
        if 0 <= curr * 2 <= 100000 and not visited[curr * 2]:
            visited[curr * 2] = visited[curr] + 1
            queue.append(curr * 2)

bfs(n)
