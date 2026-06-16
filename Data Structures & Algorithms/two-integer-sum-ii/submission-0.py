class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            sumNum = numbers[start] + numbers[end]

            if sumNum == target:
                return [start + 1, end + 1]
            elif sumNum < target:
                start += 1
            else:
                end -= 1
        
        return []
