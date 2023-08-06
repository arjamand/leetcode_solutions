class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1, row_2, row_3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        final_list = []
        temp_word1 = ""
        temp_word2 = ""
        temp_word3 = ""
        for i in words :
            for j in i.lower() :
                if j in row_1 :
                    temp_word1 += j
                if j in row_2 :
                    temp_word2 += j
                if j in row_3 :
                    temp_word3 += j
                    
            if temp_word1 == i.lower() :
                final_list.append(i)
            
            elif temp_word2 == i.lower() :
                final_list.append(i)
                
            elif temp_word3 == i.lower() :
                final_list.append(i)
                
            temp_word1 = ""
            temp_word2 = ""
            temp_word3 = ""
                
        return final_list 
            
        