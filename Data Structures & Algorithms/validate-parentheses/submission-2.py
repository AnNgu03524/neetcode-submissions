class Solution:
    def isValid(self, s: str) -> bool:

        # setup dictionary: close brackets -> open brackets
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        # setup stack
        stack = []

        # traverse string in one pass
        for bracket in s:
            # open brackets get added to the stack
            if bracket in closeToOpen.values(): 
                stack.append(bracket)
            
            # a closed bracket must match type to the top of the stack
            else:
                if not stack or stack[-1] != closeToOpen[bracket]:
                    return False
                stack.pop()
        
        # check there are no hanging open brackets after all string processed
        return False if stack else True
