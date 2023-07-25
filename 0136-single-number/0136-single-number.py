class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count1 = 0
        while 1 :
            if nums.count(nums[count1]) == 1 :
                return nums[count1]
                break
            else :
                count1 += 1
        
        
