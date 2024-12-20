class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            diff = (target - nums[i]) 
            if(diff in hash):
                return [i, hash.get(diff)]
            else:
                hash[nums[i]]=i
            
