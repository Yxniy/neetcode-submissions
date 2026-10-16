class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    x = stack.pop()
                    res[x] = i - x
                
                stack.append(i)

        

        return res

