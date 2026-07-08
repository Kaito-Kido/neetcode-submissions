class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        l = len(nums1) + len(nums2)
        k = (l + 1) // 2 # number of smallest elements in two arrays
        
        left = 0
        right = min(len(nums1), k)
        
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = k - mid1
            if mid1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[mid1 - 1]
                
            if mid1 == len(nums1):
                right1 = float("inf")
            else:
                right1 = nums1[mid1]
            
            
            if mid2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[mid2 - 1]
            if mid2 == len(nums2):
                right2 = float("inf")
            else:
                right2 = nums2[mid2]
            
            if left1 <= right2 and left2 <= right1:
                if l % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1