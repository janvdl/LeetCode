from typing import List 

class Solution:
    # dictionary to keep track of past results
    rowdict = {}
    rowdict[1] = [1]
    rowdict[2] = [1, 1]

    # generator for individual rows
    def make_row(self, rowNum):
        if rowNum not in self.rowdict:
            # initialise new row with starting 1
            tmprow = [1]

            # recursively generate previous rows
            prevrow = self.make_row(rowNum - 1)
            for k in range(len(prevrow) - 1):
                tmprow.append(prevrow[k] + prevrow[k + 1])

            # add trailing 1
            tmprow.append(1)
            
            # add to dictionary
            self.rowdict[rowNum] = tmprow

        return self.rowdict[rowNum]

    # generator for combined rows
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = []
        for i in range(1, numRows + 1):
            tmp.append(self.make_row(i))

        return tmp