class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = (s.replace("-", "")).upper()
        first_g_len = len(new_s) % k
        new_group = ""
        final_list = []
        final_key = ""
        
        if first_g_len != 0 :
            final_list.append(new_s[:first_g_len])
            new_s = new_s.replace(final_list[0],"",1)

        for i in new_s :
            if len(new_group) < k :
                new_group += i 
                if len(new_group) == k :
                    final_list.append(new_group)
                    new_group = ""
                        
        for l, j in enumerate(final_list) :
            final_key += j
            if l == len(final_list)-1:
                pass
            else :
                final_key += "-"

        return final_key
        
            
        
            
         
                
                
        
        