from typing import List

class Solution:
    def triangularNumber(self, n):
        return (n * (n + 1)) / 2

    def getDescentPeriods(self, prices: List[int]) -> int:
        counters: List[int] = []
        counter = 1

        for i in range(0, len(prices) - 1):
            if prices[i] - prices[i + 1] == 1:
                counter += 1
            else:
                counters.append(counter)
                counter = 1
        counters.append(counter)

        #print(counters)

        total = int(sum([self.triangularNumber(x) for x in counters]))
        #print(total)

        return total

    
s = Solution()
s.getDescentPeriods([3, 2, 1, 4])
s.getDescentPeriods([8, 6, 7, 7])
s.getDescentPeriods([1])