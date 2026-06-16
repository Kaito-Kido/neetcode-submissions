class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the row
        seen = set()

        for r in range(len(board)):
            seen.clear()
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in seen:
                    return False
                
                seen.add(board[r][c])

        for c in range(len(board[0])):
            seen.clear()
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue

                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for i in range(3):
            for j in range(3):
                seen.clear()
                for r in range(i * 3, i * 3 + 3):
                    for c in range(j * 3, j * 3 + 3):
                        if board[r][c] == ".":
                            continue

                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        
        return True
                        



