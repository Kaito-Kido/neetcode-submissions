class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        currentString = ""

        def backtrack(openNum, closeNum, currentString):
            if openNum < closeNum:
                return
            elif openNum == n and closeNum == n:
                result.append(currentString)
                return

            if openNum < n:
                openNum += 1
                currentString += "("
                backtrack(openNum, closeNum, currentString)
                currentString = currentString[:-1]
                openNum -= 1
            if closeNum < openNum:
                closeNum += 1
                currentString += ")"
                backtrack(openNum, closeNum, currentString)
                currentString = currentString[:-1]
                closeNum -= 1
        
        backtrack(0, 0, currentString)
        return result

            