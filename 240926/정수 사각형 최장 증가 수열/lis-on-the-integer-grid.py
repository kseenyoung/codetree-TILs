import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(i, j, count):
    if answer[i][j] > count:
        return False
    
    for d in range(4):
        row = i + dr[d]
        col = j + dc[d]
        if -1 < row < n and -1 < col < n and board[i][j] < board[row][col] and not visited[row][col]:
            visited[row][col] = True
            answer[row][col] = max(answer[row][col], count+1)
            dfs(row, col, count+1)
            visited[row][col] = False

for i in range(n):
    for j in range(n):
        visited[i][j] = True
        answer[i][j] = max(answer[i][j], 1)
        dfs(i, j, 1)
        visited[i][j] = False

result = 0
for a in answer:
    result = max(result, max(a))

print(result)