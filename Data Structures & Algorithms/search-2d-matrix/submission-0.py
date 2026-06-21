class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []

        for row in matrix:
            for num in row:
                flat_matrix.append(num)

        left = 0
        right = len(flat_matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if flat_matrix[mid] == target:
                return True
            elif flat_matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        