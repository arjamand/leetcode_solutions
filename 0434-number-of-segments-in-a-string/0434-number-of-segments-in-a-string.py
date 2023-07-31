import re
class Solution:
    def countSegments(self, s: str) -> int:
        s =  str(re.sub(' +', ' ', s.strip()))
        if s == "":
            return 0
        else :
            return (s.count(" ")+1)
        