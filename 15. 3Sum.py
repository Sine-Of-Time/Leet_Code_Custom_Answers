class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = [] 
        nums.sort() #Sorting values as this is required for the following logic to work
        for i in range(len(nums) - 1): 
            if i > 0 and nums[i] == nums[i - 1]:  # Added check to skip duplicate base values
                continue
            base = nums[i] #Updates base moving from 0 to n
            l, r = i + 1, len(nums) - 1
            while l < r: #Ensures each pointer stays on its side of the arr to avoid redundant searches and maintain search range
                total = base + nums[l] + nums[r] #Getting the sum
                if total > 0: #If the sum is to large, we decrease the right pointer to get an smaller value
                    r -= 1
                elif total < 0:#If the sum is to small, we increase left pointer to get an larger value
                    l += 1
                else:#This means values sum to 0
                    sol.append([base, nums[l], nums[r]]) #Adding values to solution array
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # Added boundary check to avoid IndexError and skip duplicate values
                        l += 1 #Skiping dulicates
        return sol
