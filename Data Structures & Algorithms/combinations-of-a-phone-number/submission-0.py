class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap = dict()
        digitmap["1"] = ""
        digitmap["2"] = "abc"
        digitmap["3"] = "def"
        digitmap["4"] = "ghi"
        digitmap["5"] = "jkl"
        digitmap["6"] = "mno"
        digitmap["7"] = "pqrs"
        digitmap["8"] = "tuv"
        digitmap["9"] = "wxyz"

        result = []
        currentstring = ""

        def backtrack(index, currentstring):
            if index == len(digits):
                if currentstring == "":
                    return
                result.append(currentstring)
                return


            chars = digitmap[digits[index]]
            for char in chars:
                backtrack(index + 1, currentstring + char)
        backtrack(0, currentstring)
        return result

