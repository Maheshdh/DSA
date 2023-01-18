class Solution:
    # Time complexity : O(n)
    # Space complexity : O(1)
    # [val1, val2, n , n+1,...]
    # for each value, if we consider that value, we can consider max sum before considering it's previous value, else, if we do not consider that value, we consider the max value we can obtain just upto previous value

    def rob(self, nums: List[int]) -> int:
        val1 , val2 = 0,0

        for val in nums:
            temp = max(val1+val,val2)
            val1 = val2
            val2 = temp

        return val2
