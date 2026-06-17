class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max, suffix_max = [0,], []
        water = 0
        for i in range(1, len(height)):
            prefix_max.append(max(height[:i]))
        for i in range(0, len(height)-1):
            suffix_max.append(max(height[i:]))
        suffix_max.append(0)
        print(prefix_max, suffix_max)

        for i in range(len(height)):
            trap = min(suffix_max[i], prefix_max[i]) - height[i]
            if trap > 0:
                water += trap
            print(i, prefix_max[i], suffix_max[i], trap, water)
            
        return water