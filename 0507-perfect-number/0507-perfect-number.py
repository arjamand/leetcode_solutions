class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 :
            return False

        factors_list = [i for i in range(1, int(num**0.5) + 1) if num % i == 0 and i != num] + [num // i for i in range(1, int(num**0.5) + 1) if num % i == 0 and i != num // i and i != num]

        factors_list.pop(factors_list.index(num))

        if sum(factors_list) == num :
            return True
        else:
            return False