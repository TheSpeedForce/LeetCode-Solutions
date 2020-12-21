class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            amount = sum(i)
            if amount > rich:
                rich = amount
        return rich
