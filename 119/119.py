from typing import List

class Solution:
    # dictionary to keep track of past results
    rowdict = {}
    rowdict[0] = [1]
    rowdict[1] = [1, 1]
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex not in self.rowdict:
            # initialise new row with starting 1
            tmprow = [1]

            # recursively generate previous rows
            prevrow = self.getRow(rowIndex - 1)
            for k in range(len(prevrow) - 1):
                tmprow.append(prevrow[k] + prevrow[k + 1])

            # add trailing 1
            tmprow.append(1)
            
            # add to dictionary
            self.rowdict[rowIndex] = tmprow

        return self.rowdict[rowIndex]
    
s = Solution()
print(s.getRow(3))