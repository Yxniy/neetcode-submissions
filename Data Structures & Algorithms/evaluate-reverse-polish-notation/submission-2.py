class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp = ['*','/','+','-']
  
       
        for n in tokens:
            if n not in opp:
                stack.append(int(n))
            else:
                x = stack.pop()
                y = stack.pop()

                if n == '*':
                    stack.append(y * x)
                elif n == '+':
                    stack.append(y + x)
                elif n == '-':
                    stack.append(y - x)
                elif n == '/':
                    stack.append(int(y/x))
        
        return stack[0]
            


        