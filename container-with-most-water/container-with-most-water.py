class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        sol = 0
        max_h = max(height)
        while i < j:
            
            min_ht = min(height[i],height[j])
            breadth = j - i
            sol = max(sol,min_ht * breadth)
            if breadth * max_h <= sol:
                break
            if height[i] < height[j]:
                i += 1
                while i < j and height[i] < height[i-1]:
                    i += 1
            else:
                j -=1
                while i < j and height[j+1] >= height[j]:
                    j -= 1
            
        return sol
        
        