class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        totaltank = 0
        currtank = 0
        startstation = 0

        for i in range(len(gas)):
            netgain = gas[i] - cost[i]
            currtank += netgain

            if currtank < 0:
                startstation = i+1
                currtank = 0
        return startstation 