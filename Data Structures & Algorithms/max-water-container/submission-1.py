class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0
        while l<r:
            if heights[l] >= heights[r]:
                m = heights[r]*(r-l)
                maxArea = max(maxArea, m)
                r -= 1
            else:
                m = heights[l]*(r-l)
                maxArea = max(maxArea, m)
                l += 1
        return maxArea
        