class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        i = 0
        bracks = {'{':'}', '[': ']', '(':')'}
        while i < len(s):
            if s[i] in bracks:
                my_stack.append(s[i])
                i +=1
            if s[i] in bracks.values():
                if my_stack:
                    if s[i] == bracks[my_stack[-1]]:
                        my_stack.pop()
            i +=1 
        return not my_stack
        
            