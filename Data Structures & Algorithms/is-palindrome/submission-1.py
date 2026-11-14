class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Setup pointers
        L = 0
        R = len(s) - 1

        # Clean case sensitivity
        cleanedString = s.lower()

        # Check equality
        while (L < R):
            charL, charR = cleanedString[L], cleanedString[R]

            # Skip non alphanumeric characters
            if not charL.isalnum():
                L += 1
                continue
            if not charR.isalnum():
                R -=1
                continue

            # Check symmetry
            if charL != charR:
                return False
            else:
                L += 1
                R -= 1
        return True

        


        