class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        bracks = {')':'(' , '}':'{', ']' :'['}
        for i in s:
            if i in bracks:
                if my_stack and bracks[i] == my_stack[-1]:
                        my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(i)
        return True if not my_stack else False