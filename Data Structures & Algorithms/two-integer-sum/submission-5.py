class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in vals:
                return [vals[complement], i]
            vals[nums[i]] = i
            
                

        