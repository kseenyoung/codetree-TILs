import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]

sorted_list = []
for i in range(n):
    for j in range(n):
        sorted_list.append((board[i][j], i, j))

sorted_list.sort()
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for _, i, j in sorted_list:
    for d in range(4):
        row, col = i+dr[d], j+dc[d]
        if -1 < row < n and -1 < col < n and board[i][j] < board[row][col] and dp[i][j]+1 > dp[row][col]:
            dp[row][col] = dp[i][j]+1

answer = 0
for d in dp:
    answer = max(answer, max(d))

print(answer)