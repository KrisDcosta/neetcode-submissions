class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max, suffix_max = [0]*n, [0]*n
        water = 0
        for i in range(1, n):
            prefix_max[i] = max(height[:i])
        for i in range(0, n-1):
            suffix_max[i] = max(height[i:])

        for i in range(n):
            trap = min(suffix_max[i], prefix_max[i]) - height[i]
            if trap > 0:
                water += trap            
        return water