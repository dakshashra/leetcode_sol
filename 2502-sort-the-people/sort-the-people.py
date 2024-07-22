class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        ans=[]
        while True:
            try:
                mn=heights.index(max(heights))
                ans.append(names[mn])
                heights.pop(mn)
                names.pop(mn)
            except:
                break
        return ans