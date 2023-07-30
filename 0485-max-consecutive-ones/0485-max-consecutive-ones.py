class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        counts = [] 
        for i in nums :
            if i == 1 :
                count += 1
            else :
                counts.append(count)
                count = 0
            counts.append(count)
        return max(counts)