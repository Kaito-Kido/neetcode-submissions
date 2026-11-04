class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        path = []
        colset = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                output.append(path.copy())
                return

            for col in range(n):
                rowstring = "".join(["." for i in range(n)])
                if col not in colset and (row + col) not in diag1 and (col - row) not in diag2:
                    rowstring =  rowstring[:col] + "Q" + rowstring[col + 1:]
                    path.append(rowstring)
                    colset.add(col)
                    diag1.add(row + col)
                    diag2.add(col - row)
                    backtrack(row + 1)
                    path.pop()
                    colset.remove(col)
                    diag1.remove(row + col)
                    diag2.remove(col - row)
        backtrack(0)
        return output



