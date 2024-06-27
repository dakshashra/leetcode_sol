class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        x=edges[0][0]
        y=edges[0][1]
        if x in edges[1]:
            return x
        return y