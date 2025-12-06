class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # this is just math
        # (a + bi)(c + di) = ac - bd + (ad + bc)i
        a, b = map(int, num1.replace("i", "").split("+"))
        c, d = map(int, num2.replace("i", "").split("+"))
        
        real = a*c - b*d
        imaginary = a*d + b*c
        result = str(real) + "+" + str(imaginary) + "i"
        return result
    
s = Solution()
print(s.complexNumberMultiply("1+1i", "1+1i"))
print(s.complexNumberMultiply("1+-1i", "1+-1i"))