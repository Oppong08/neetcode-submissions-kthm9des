class Solution:
    def isValid(self, s: str) -> bool:
        #build brackets map 
        bracksmap = {')':'(' , '}':'{', ']' :'['}
        stack = []
        for i in s:
            #if its a closing bracket
            if i in bracksmap:
                if stack and bracksmap[i]== stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
            #if its an opening bracket
                stack.append(i)
        return True if not stack else False








        # my_stack = []
        # bracks = {')':'(' , '}':'{', ']' :'['}
        # for i in s:
        #     if i in bracks:
        #         if my_stack and bracks[i] == my_stack[-1]:
        #                 my_stack.pop()
        #         else:
        #             return False
        #     else:
        #         my_stack.append(i)
        # return True if not my_stack else False