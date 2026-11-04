class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        currentString = ""

        def backtrack(openNum, closeNum, currentString):
            if openNum > closeNum:
                return
            elif openNum == 0 and closeNum == 0:
                result.append(currentString)

            if openNum > 0:
                openNum -= 1
                currentString += "("
                backtrack(openNum, closeNum, currentString)
                currentString = currentString[:-1]
                openNum += 1
            if closeNum > 0:
                closeNum -= 1
                currentString += ")"
                backtrack(openNum, closeNum, currentString)
                currentString = currentString[:-1]
                closeNum += 1
        
        backtrack(n, n, currentString)
        return result

            