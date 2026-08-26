class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[' :
                stack.append(c)
            elif not stack:
                return False
            elif c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            else:
                if stack[-1] != '[':
                    return False
                stack.pop()

        if not stack:
            return True
        return False