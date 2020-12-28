class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high = max(candies)
        for i in range(len(candies)):
            candy = candies[i]
            greatest = False
            if candy + extraCandies >= high:
                greatest = True
            candies[i] = greatest
        return candies
                
