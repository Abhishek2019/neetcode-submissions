class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        current_fuel = 0
        start = 0
        total_fuel = 0

        for i in range(len(gas)):

            current_fuel = current_fuel+gas[i]-cost[i]
            total_fuel = total_fuel+gas[i]-cost[i]

            if current_fuel<0:
                start = i+1
                current_fuel = 0

        return start if total_fuel>=0 else -1


        

