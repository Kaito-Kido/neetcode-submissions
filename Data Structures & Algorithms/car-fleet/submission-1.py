class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        time = [(target - p) / s for p, s in cars]
        fleetCount = 0
        print(time)
        
        maxTime = -1

        for t in time:
            if t > maxTime:
                maxTime = t
                fleetCount += 1
        return fleetCount

        
