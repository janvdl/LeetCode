class Solution:
    def countCollisions(self, directions: str) -> int:
        crashes = 0
        r_count = 0

        obstacle_left = False
        for d in directions:
            if d == "L":
                if r_count != 0:
                    crashes += r_count + 1
                    r_count = 0
                    obstacle_left = True
                elif obstacle_left:
                    crashes += 1
            elif d == "S":
                if r_count > 0:
                    crashes += r_count
                    r_count = 0

                obstacle_left = True
            elif d == "R":
                r_count += 1

            else:
                print("You dun goofed")
        
        return crashes
 
s = Solution()
print(s.countCollisions("RLRSLL")) # 4 counts
print(s.countCollisions("LLRR")) # 0 counts
print(s.countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")) # 20
print(s.countCollisions("LRLLLRSRRRSRLSSLLSSSLRSRLSRLRLRLSLRSR")) # 24