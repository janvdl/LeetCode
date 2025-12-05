from typing import *
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        midpoint = (len(nums1) + len(nums2) + 1) / 2
        single_mid = True
        if midpoint != round(midpoint):
            single_mid = False
            midpoint = math.ceil(midpoint)

        tmp = []
        while len(tmp) < midpoint:
            num = None

            if len(nums1) > 0 and len(nums2) > 0:
                num = nums1.pop(0) if nums1[0] <= nums2[0] else nums2.pop(0)
            elif len(nums1) > 0:
                num = nums1.pop(0)
            else:
                num = nums2.pop(0)

            tmp.append(num)
                
        return tmp[-1] if single_mid else (tmp[-1] + tmp[-2]) / 2
    
s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))