class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # in any sequential range of n integers there are 2 possibilities
        #   (n // 2) are odd if the first number is even
        #   (n // 2) + 1 are odd if the first and last numbers are odd
        n = high - low + 1
        odds = n >> 1
        odds += 1 if low % 2 != 0 and high % 2 != 0 else 0
        
        return odds

s = Solution()
print(s.countOdds(3, 7))
print(s.countOdds(8, 10))
print(s.countOdds(21, 22))