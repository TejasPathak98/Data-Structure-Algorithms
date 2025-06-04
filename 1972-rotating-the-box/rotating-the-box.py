class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        for row in boxGrid:
            write = n - 1
            for col in reversed(range(n)):
                if row[col] == "*":
                    write = col - 1
                elif row[col] == "#":
                    row[col] = "."
                    row[write] = "#"
                    write -= 1
        
        new_box = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_box[j][m - 1 - i] = boxGrid[i][j]

        return new_box

