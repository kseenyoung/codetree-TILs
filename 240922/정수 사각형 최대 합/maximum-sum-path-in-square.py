from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = [[0]*N for _ in range(N)]

que = deque()
que.append((0, 0, 0))

while que:
    row, col, val = que.popleft()
    answer[row][col] = max(answer[row][col], val+board[row][col])

    if row+1 < N:
        que.append((row+1, col, val+board[row][col]))
    if col+1 < N:
        que.append((row, col+1, val+board[row][col]))

print(answer[N-1][N-1])