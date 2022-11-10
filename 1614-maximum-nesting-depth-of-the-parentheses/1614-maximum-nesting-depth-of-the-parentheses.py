class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        curr_depth = 0
        for c in s:
            if c == "(":
                curr_depth +=1
                depth = max(depth,curr_depth)
            elif c == ")":
                curr_depth -=1
        return depth
                
            