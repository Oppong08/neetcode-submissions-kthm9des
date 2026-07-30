class Solution:
    def decodeString(self, s: str) -> str:
        #logic: loop through the input string, add all characters to the stack. 
        #if the current character is a "]", pop all elements up until the opening bracket extract the digit that comes before the opening bracket and multiply the substring poped by it
        #add the substring back to the stack.
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr

                #pop out the open bracket
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
            
                stack.append(int(k) * substr)
        return "".join(stack)

        
