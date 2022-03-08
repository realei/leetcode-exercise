class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        prev = [1, 1]
        for i in range(2, rowIndex+1):
            j = 0
            cur = []
            while(j<=i):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(prev[j] + prev[j-1])
                j+=1

            prev = cur

        return cur        
