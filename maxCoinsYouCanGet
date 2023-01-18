class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        my_choices=piles[len(piles)//3::2]
        return sum(my_choices)
