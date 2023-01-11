class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        total = len(nums1) + len(nums2)
        half = total//2
        l=0
        r=len(nums1)-1
        while True:
            i = (l+r)//2
            j = half - i - 2
            if i>=0:
                A_left = nums1[i]
            else:
                A_left = -float('inf')
            if j>=0:
                B_left = nums2[j]
            else:
                B_left = -float('inf')
            if i+1<len(nums1):
                A_right = nums1[i+1]
            else:
                A_right = float('inf')
            if j+1<len(nums2):
                B_right = nums2[j+1]
            else:
                B_right = float('inf')
            
            if A_left<=B_right and B_left<=A_right:
                if total%2:
                    return min(A_right,B_right)
                else:
                    return (max(A_left,B_left)+min(A_right,B_right))/2
            else:
                if A_left>B_right:
                    r=i-1
                else:
                    l=i+1
            


        
