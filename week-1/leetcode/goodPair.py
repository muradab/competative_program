class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairCount = 0 ;
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] == nums[j]):
                    pairCount += 1
                
        return pairCount
        