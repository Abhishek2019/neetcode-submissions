from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        c = Counter(hand)

        for ele in sorted(c):

            curr_freq = c[ele]

            if curr_freq>0:

                for i in range(ele,ele+groupSize):

                    if c[i] < curr_freq:
                        return False

                    c[i]-=curr_freq

        return True

        
        