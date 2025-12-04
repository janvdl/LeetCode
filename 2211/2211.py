class Solution:
    def countCollisions(self, directions: str) -> int:
        count = 0
        collisions = ["RRRRRRRRRRS", "SLLLLLLLLLL", "RS", "SL"]

        # resolve the RL collisions so that only RS and SL collisions remain
        count += directions.count("RL") * 2
        directions = directions.replace("RL", "S")

        while any(x in directions for x in collisions):
            for x in collisions:
                if x in directions:
                    count += (len(x) - 1) * (directions.count(x))
                    directions =  directions.replace(x, "S")
        
        return count