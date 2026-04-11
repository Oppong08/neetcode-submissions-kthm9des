class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif i == "-":
                res = abs(stack.pop() - stack.pop())
                stack.append(res)
            elif i == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif i == "/":
                pop1, pop2 = stack.pop(), stack.pop()
                res = pop2/pop1
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]

                    
        