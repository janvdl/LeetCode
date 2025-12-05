from typing import *

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            p1 = sum(nums[:i]) % 2 == 0 
            p2 = sum(nums[i:]) % 2 == 0

            if (p1 and p2) or (not p1 and not p2):
                count += 1
        return count
    
s = Solution()
print(s.countPartitions([10, 10, 3, 7, 6]))
print(s.countPartitions([1,2,2]))
print(s.countPartitions([2,4,6,8]))
print(s.countPartitions([2]))