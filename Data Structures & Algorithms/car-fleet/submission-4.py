class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        pos_speed = zip(position, speed)

        pos_speed = sorted(pos_speed, key=lambda x:x[0], reverse=True)

        count = 1

        stck = []
        for p,s in pos_speed:

            time = (target-p)/s

            if not stck:
                stck.append(time)

            else:

                if stck[-1] < time:
                    count+=1
                    stck.append(time)



        return count