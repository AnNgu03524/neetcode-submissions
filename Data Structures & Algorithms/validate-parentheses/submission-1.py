class Solution:
    def isValid(self, s: str) -> bool:
        # setup stack
        stack = []

        # setup map: close-parenth -> open-parenth
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        # pass through string
        for char in s:
            # open brackets get added to stack
            if char in closeToOpen.values():
                stack.append(char)
            # close brackets - check it matches the latest stack item
            elif stack and stack[-1] == closeToOpen[char]:      # the first statement prevents an index out of range error
                stack.pop()
            else:
                return False
        # check no more hanging open brackets
        return False if stack else True     # return value_if_true if condition else value_if_false   

        

        



        