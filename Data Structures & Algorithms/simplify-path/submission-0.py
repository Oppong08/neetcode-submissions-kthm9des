class Solution:
    def simplifyPath(self, path: str) -> str:

        #use stack for poping at ".."
        stack = []
        #start building a path after a "/". add cur to stack at the next "/" after checks
        cur = ""
        for c in path + "/":
            if c == "/":
                #double dots means move out to the previous root
                if cur == "..":
                    if stack:
                        stack.pop()
                #ignore single dots
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)