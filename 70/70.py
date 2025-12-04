class Solution:
    stepdict = {}
    stepdict[1] = 1
    stepdict[2] = 2
    def climbStairs(self, n: int) -> int:
        if n not in self.stepdict:
            for i in range(1, n + 1):
                if i not in self.stepdict:
                    self.stepdict[i] = self.stepdict[i - 1] + self.stepdict[i - 2]

        return self.stepdict[n]
