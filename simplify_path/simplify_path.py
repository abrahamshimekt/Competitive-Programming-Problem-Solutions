class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for index in range(len(path)):
            if stack and path[index] == "..":
                stack.pop()
            elif path[index] != ".." and path[index] != "." and path[index] != "/" and path[index] != "":
                stack.append(path[index])
        return '/'+'/'.join(stack)
        
        