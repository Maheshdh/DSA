class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity : O(n)
        # Space complexity : O(n)
        
        seen = set()
        for val in nums:
            if val in seen:
                return True
            else:
                seen.add(val)
        return False
