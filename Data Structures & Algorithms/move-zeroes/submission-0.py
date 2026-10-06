class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        n = len(nums)
        c = 0
        ans = []

        for i in range(n):
            if nums[i] != 0:
                ans.append(nums[i])
                c  += 1

        for i in range(n):
            if i<c:
                nums[i] = ans[i]
            else:
                nums[i] = 0


        nums = ans

        return ans
        