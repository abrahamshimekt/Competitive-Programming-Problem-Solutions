class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        par = {")":"("}
        total_score = 0
        for index in range(len(s)):
            if stack and stack[-1][0] == par.get(s[index],None):
                bracket,curr_score = stack[-1]
                curr_score *= 2
                stack.pop()
                if curr_score == 0:
                    curr_score = 1
                if stack:
                    stack[-1][1] += curr_score
                else:
                    total_score += curr_score
            else:
                stack.append([s[index],0])
        return total_score

        