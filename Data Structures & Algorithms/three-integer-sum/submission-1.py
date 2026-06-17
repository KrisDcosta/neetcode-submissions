class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = [nums[i], nums[j], nums[k]]
                        a.sort()
                        if a not in valid:
                            valid.append(a)
        return valid