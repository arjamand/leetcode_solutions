class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = str(bin(num)[2:])
        new_str = ""
        for i in binary_str :
            if int(i) == 0 :
                new_str += "1"
            elif int(i) == 1 :
                new_str += "0"

        return int(f"{new_str}",2)
