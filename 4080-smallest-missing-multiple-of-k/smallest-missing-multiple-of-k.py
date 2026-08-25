class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_set = set(nums)
        current_multiple = k
        
        while current_multiple in num_set:
            current_multiple += k
            
        return current_multiple
