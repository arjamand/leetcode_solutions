class Solution:
    def isPalindrome(self, x: 121) -> bool:
       
        if str(x)[::-1] == str(x):
            return True 
        else :
            return False