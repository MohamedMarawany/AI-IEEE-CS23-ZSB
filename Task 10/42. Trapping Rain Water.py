class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = water_volume = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left]) 
                water_volume += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right]) 
                water_volume += right_max - height[right]
                right -= 1
        
        return water_volume