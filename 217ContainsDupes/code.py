class Solution(object):
    def containsDuplicate(self, nums):
        
        #check if number is in set and then add into it with all the numbers, if number is seen then return true else false
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
