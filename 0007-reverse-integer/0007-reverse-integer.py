class Solution:
    def reverse(self, x: int) -> int:
        
        if str(x)[0] != "-" and int(str(x)[::-1]) > 2147483647 :
            return 0
        if str(x)[0] == "-" :           
            new_s = str(x).replace("-","")
            if int("-"+(new_s[::-1])) < -2147483648 :
                return 0
            else :
                return int("-"+(new_s[::-1]))    
        else:
            return int(str(x)[::-1])

