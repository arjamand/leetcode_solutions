class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        x = 0
        while len(str_num ) > 1 :
            for i in str_num :
                x += int(i)
            str_num = str(x)
            x = 0
            
        return int(str_num)
                
        