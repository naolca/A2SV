class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = ["N", 'W', "E", 'S']
        instructions *= 4
        curr = "N"
        pos = [0, 0]
        for di in instructions:
            if di == "G":
                if curr == "N":
                    pos[1] += 1
                elif curr == "E":
                    pos[0] += 1
                elif curr == "W":
                    pos[0] -= 1
                else:
                    pos[1] -= 1
                
            elif di == "L":
                if curr == "N":
                    curr = "W"
                elif curr == "E":
                    curr = "N"
                elif curr == "W":
                    curr = "S"
                else:
                    curr = "E"
            else:
                if curr == "N":
                    curr = "E"
                elif curr == "E":
                    curr = "S"
                elif curr == "W":
                    curr = "N"
                else:
                    curr = "W"
            print(pos)
        return pos == [0, 0]

                    
        
