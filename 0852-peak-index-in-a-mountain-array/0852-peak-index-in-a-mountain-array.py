class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i_v = 0
        if len(arr) >= 3 :
            for i in arr :
                if i > i_v  :
                    i_v = i 
            if arr.index(i_v) < (len(arr)-1) and arr.index(i_v) > 0 :
                i = arr.index(i_v)
                return i
                
                    
         