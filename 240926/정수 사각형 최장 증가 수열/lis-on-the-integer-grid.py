import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [[1]*n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(i, j):
    que = deque()
    que.append((i, j, 1))

    while que:
        row, col, val = que.popleft()
        if answer[row][col] > val:
            continue

        for d in range(4):
            r = row + dr[d]
            c = col + dc[d]
            if -1 < r < n and -1 < c < n and answer[r][c] < val+1 and board[row][col] < board[r][c]:
                answer[r][c] = val+1
                que.append((r, c, val+1))

for i in range(n):
    for j in range(n):
        bfs(i, j)

result = 0
for a in answer:
    result = max(result, max(a))
print(result)