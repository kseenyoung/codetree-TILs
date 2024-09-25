import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

que = deque()
que.append((0, 0, board[0][0]))
answer = 0

while que:
    row, col, val = que.popleft()
    if row == n-1 and col == n-1:
        answer = max(answer, val)
        continue
    
    if row+1 < n and col < n:
        que.append((row+1, col, min(val, board[row+1][col])))
    if col+1 < n and col < n:
        que.append((row, col+1, min(val, board[row][col+1])))

print(answer)