import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        out = sorted(zip(position,speed), reverse=True)


        fleet = 0
        max_turns = 0
        for car in out:

            turns_to_reach_target = (target-car[0])/car[1]

            if turns_to_reach_target > max_turns:

                fleet+=1
                max_turns = turns_to_reach_target

        return fleet

        