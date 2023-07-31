class Solution:
    def arrangeCoins(self, n: int) -> int:         
        coin_count = 0
        coin_amount = 0
        for i in range (1, n+1) :
            if coin_amount + i <= n :
                coin_amount+=i
                coin_count += 1
                
            elif coin_amount + i > n :
                break
        return (coin_count)


            
            
        