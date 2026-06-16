class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operationSet = {"+", "-", "*", "/"}
        for op in tokens:
            print(op)
            print(stack)
            if op in operationSet:
                b = stack.pop()
                a = stack.pop()
                if op == "+":
                    stack.append(b + a)
                elif op == "-":
                    stack.append(a - b)
                elif op == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(op)) 
        return stack.pop()
            
