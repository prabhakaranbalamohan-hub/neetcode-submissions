class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        newList = set()
        for x in nums:
            if x in newList:
                return True
            newList.add(x)
        return False        
    