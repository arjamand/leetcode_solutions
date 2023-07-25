class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] == 9 :
        #     digits[-1] = (1)
        #     digits.append(0)
        # else:
        #     digits[-1] = ((digits[-1])+1)
            
        # return digits

        s_d = ""
        for d in digits :
            s_d = "".join([s_d,str(d)])
        s_d = int(s_d)+1
        s_d_2 = str(s_d)
        digits = []
        for l in s_d_2 :
            digits.append(int(l))

        return digits

        
