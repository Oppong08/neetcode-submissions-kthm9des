class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                if stack:
                    stack.append(int(stack[-1]) + int(stack[-1]))

            elif operations[i] == "D":
                stack.append(2 * int(stack[-1]))

            elif operations[i] == "C":
                stack.pop()

            else:
                stack.append(int(operations[i]))

        return sum(stack)