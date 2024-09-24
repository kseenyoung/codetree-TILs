import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n) for _ in range(n)]
dp[0][0] = board[0][0]

# 초기화
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + board[0][j]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + board[i][0]

# print(dp)

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j]+board[i][j], dp[i][j-1]+board[i][j])

print(dp[n-1][n-1])