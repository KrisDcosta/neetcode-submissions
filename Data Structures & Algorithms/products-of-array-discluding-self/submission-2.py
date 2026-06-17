class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # for i in range(len(nums)):
        #     pdt = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             pdt *= nums[j]
        #     output.append(pdt)
        # n = len(nums)
        # output = [0]*n
        # pref, suff = [0]*n, [0]*n
        # pref[0] = suff[n-1] = 1
        # for i in range(1,n):
        #     pref[i] = nums[i-1] * pref[i-1]
        # for i in range(n-2,-1,-1):
        #     suff[i] = nums[i+1] * suff[i+1]
        # output = [pref[i]*suff[i] for i in range(n)] 
        output = [1]*(len(nums)) 
        prefix, suffix = 1, 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
        return output