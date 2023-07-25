class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        while 1 :
            try :
                nums.remove(val)
            except :
                break
        return len(nums)+1


        