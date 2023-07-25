class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

                
        num_count = 0
        rep_count  = 0
        for num in nums :
            rep_count = 0
            for rep in nums :
                if num + rep == target and rep_count != num_count:
                        return[num_count,rep_count]
                        break
                rep_count += 1
            num_count += 1
            