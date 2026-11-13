import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Set upper and lower possible speed
        sLeft = 1
        sRight = max(piles)

        # Binary 'search' for the minimum speed
        # Can I prove that binary searching for the speed is more effective than approaching from the bottom?
        while(True):
            # Get middle
            sMid = sLeft + (sRight-sLeft)//2

            # minimum succcessful eating speed found
            if sLeft == sRight:
                return sMid
            # successful eating rate, check left for smaller val inclusive of current val
            if checkEatingSpeed(piles, h, sMid):
                sRight = sMid
            # eating too slow, search right exclusive of current value
            else:
                sLeft = sMid + 1
            
    

"""
validates that the eating speed can finish piles
"""
def checkEatingSpeed(piles: List[int], maxHours:int, speed:int) -> bool:
    hoursSpent = 0
    for pile in piles:
        hoursSpent += math.ceil(pile / speed) # does python automatically apply integer division for integers?
        if hoursSpent > maxHours:
            return False
    return True




        