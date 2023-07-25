class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        ans = 0
        for num in range(10):
            if ans != 1 :
                if ans != 0 :
                    str_n = 0 + ans
                    ans = 0
                    for l in str(str_n) :
                        ans += (int(l))**2
                else :
                    for l in str(str_n) :
                        ans += (int(l))**2
            if ans ==1 :
                return True
        return False
                
                