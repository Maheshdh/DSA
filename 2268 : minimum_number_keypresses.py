class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # Time complexity : O(n), where n is input size
        counts = collections.Counter(s)

        ans = count = 0

        for i, freq in enumerate(sorted(counts.values(), reverse = True)):
            if i % 9 == 0:
                count+=1
            ans = ans + (count * freq)
        
        return ans
