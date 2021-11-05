

def dfs(i, j):
    if board[i][j] == 1 or i < 0 or j < 0 or i >= n or j >= m:
        return 0

    if board[i][j] == 0:
        board[i][j] = 1
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i - 1, j)


if __name__ == '__main__':

    n, m = map(int, input().split())

    board = [list(map(int, input().rstrip())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    print(board)
    result = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                continue
            result += dfs(i, j)


