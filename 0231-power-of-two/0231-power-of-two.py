class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 0
        x = 0
        while num <=(pow(2, 31) - 1) :
            num = pow(2, x)
            x += 1 
            if num == n :
                return True
        return False    