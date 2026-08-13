class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        pref[0] = 1
        suff = [0]*n
        suff[n-1] = 1
        res = [0]*n

        for i in range(1, n):
            pref[i] = nums[i-1]*pref[i-1]

        for j in range(n-2, -1, -1):
            suff[j] = nums[j+1]*suff[j+1]

        for k in range(n):
            res[k] = pref[k]*suff[k]
        return res


        