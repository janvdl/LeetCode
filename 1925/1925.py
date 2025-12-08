class Solution:
    def countTriples(self, n: int) -> int:
        triple_count = 0
    
        for c in range(1, n + 1):
            for a in range(1, c):
                b2 = (c ** 2) - (a ** 2)
                b = int(b2 ** 0.5)
                
                if b ** 2 == b2 and 1 <= b <= n:
                    triple_count += 1

        return triple_count

s = Solution()
print(s.countTriples(18))