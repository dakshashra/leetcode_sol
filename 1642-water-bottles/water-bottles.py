class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans=numBottles
        emp=numBottles
        while emp>=numExchange:
            now=emp//numExchange

            ans+=now
            emp=now+emp%numExchange
            print('ans=', ans, 'emp=', emp, 'now=', now)
        return ans