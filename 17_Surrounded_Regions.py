class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    self.dfs(board, i, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                    
        
                    
    def dfs(self, board, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return
        
        board[i][j] = '#'
        self.dfs(board, i-1, j, m, n)
        self.dfs(board, i+1, j, m, n)
        self.dfs(board, i, j-1, m, n)
        self.dfs(board, i, j+1, m, n)