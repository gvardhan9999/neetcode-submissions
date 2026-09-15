class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxi=0

        for num in prices:
            prof=num-mini
            mini=min(mini,num)
            maxi=max(prof,maxi)

        return maxi
        