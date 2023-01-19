class Solution:
    def rob_helper(self, arr) :
        val1 , val2 = 0,0

        for val in arr:
            temp = max(val1+val,val2)
            val1 = val2
            val2 = temp

        return val2

    def rob(self, nums: List[int]) -> int:
        # Time complexity : O(n)
        # Space complexity : O(1)
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        val1 = self.rob_helper(nums[:len(nums)-1])
        val2 = self.rob_helper(nums[1:])
        return max(val1,val2)
   
