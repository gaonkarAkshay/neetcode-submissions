class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force = O(n2)
        # res = 0;

        # for l in range(len(heights)):
        #     print('l',l)
        #     for r in range(l + 1, len(heights)):
        #         print('r',r)
        #         area = (r - l) * min(heights[l], heights[r]);
        #         res = max(res, area);
        
        # return res;

        # Liner Time Solution: O(n)
        res = 0;
        l, r = 0, len(heights) - 1;

        while l < r:
            width = r - l;
            height = min(heights[l], heights[r]);
            area = width * height;
            res = max(res, area);
            if heights[l] < heights[r]:
                l += 1;
            else:
                r -= 1;

        return res
            
            









