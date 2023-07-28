class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        final_list = []

        if nums.count(target) == 1 :
            return[nums.index(target), nums.index(target)]
        elif nums.count(target) == 0 :
            return[-1,-1]
        
        for i, j in enumerate(nums) :
            if j == target :
                final_list.append(i)
                break
        for a, b in reversed(list(enumerate(nums))) :
            if b == target :
                final_list.append(a)
                return(final_list)

        
        