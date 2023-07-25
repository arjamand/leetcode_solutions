class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s[::-1] 
        count = 0
        for letter in new_s:
            if letter != " ":
                count += 1
            elif letter == " " and count == 0 :
                pass
            else :
                break
            
        return count




