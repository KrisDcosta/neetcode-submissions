class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            # Hash map is a set (count unique values), hash is a dict (count)
            set_rows = set()
            set_cols = set()
            for j in range(len(board)):
                # Checking rows
                if board[i][j] != '.':
                    if board[i][j] in set_rows:
                        return False
                    set_rows.add(board[i][j])

                # Checking cols
                if board[j][i] != '.':
                    if board[j][i] in set_cols:
                        return False
                    set_cols.add(board[j][i])

        for index in range(len(board)):
            set_grid = set()
            for i in range(3):
                for j in range(3):
                    r = (index//3)*3+i
                    c = (index%3)*3+j
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in set_grid:
                        return False
                    set_grid.add(board[r][c])
        return True