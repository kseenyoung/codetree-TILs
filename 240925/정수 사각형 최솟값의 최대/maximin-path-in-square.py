import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(board[0][0])
    exit()

# DP
dp = [[1e9]*(n+1) for _ in range(n+1)]
dp[1][1] = board[0][0]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i-1][j] == 1e9 or dp[i][j-1] == 1e9:
            dp[i][j] = min(board[i-1][j-1], dp[i-1][j], dp[i][j-1])
        elif board[i-1][j-1] > dp[i-1][j] and board[i-1][j-1] > dp[i][j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif board[i-1][j-1] < dp[i-1][j] and board[i-1][j-1] < dp[i][j-1]:
            dp[i][j] = board[i-1][j-1]
        else:
            dp[i][j] = board[i-1][j-1]
        # print(dp[i][j])

# for d in dp:
#     print(d)
# print(dp)
print(dp[n][n])
# BFS
# que = deque()
# que.append((0, 0, board[0][0]))
# answer = 0

# while que:
#     row, col, val = que.popleft()
#     if row == n-1 and col == n-1:
#         answer = max(answer, val)
#         continue
    
#     if row+1 < n and col < n:
#         que.append((row+1, col, min(val, board[row+1][col])))
#     if col+1 < n and col < n:
#         que.append((row, col+1, min(val, board[row][col+1])))

# print(answer)