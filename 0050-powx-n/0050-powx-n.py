class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 : return 0
        elif n == 0 : return 1
        else :
            return float(x**n)

        
