class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s=(s.upper())
        p_counter = (-1)

        num = 0
        for r in s :
            p_counter +=1
            if r=="I":
                num+=1
            elif r== "V":
                if s[(p_counter-1)]=="I" and p_counter != 0 :
                    num+=3
                else:
                    num+=5
            elif r=="X":
                if s[(p_counter-1)]=="I" and p_counter != 0:
                    num+=8
                else:
                    num+=10
            elif r=="L":
                if s[(p_counter-1)]=="X" and p_counter != 0:
                    num+=30
                else:
                    num+=50
            elif r=="C":
                if s[(p_counter-1)]=="X" and p_counter != 0:
                    num+=80
                else:
                    num+=100
            elif r=="D":
                if s[(p_counter-1)]=="C" and p_counter != 0:
                    num+=300
                else:
                    num+=500
            elif r=="M":
                if s[(p_counter-1)]=="C" and p_counter != 0:
                    num+=800
                else:
                    num+=1000
        return(num)

