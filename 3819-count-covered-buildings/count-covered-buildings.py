class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)

        for building in buildings:
            x,y = building

            row_dict[x].append(y)
            col_dict[y].append(x)

        
        for col in col_dict:
            col_dict[col].sort()
        
        for row in row_dict:
            row_dict[row].sort()

        
        count = 0 

        for building in buildings:

            bx,by = building

            i = bisect_left(row_dict[bx], by)
            j = bisect_left(col_dict[by], bx)

            has_left = i > 0
            has_right = i < len(row_dict[bx]) - 1

            has_up = j > 0
            has_down = j < len(col_dict[by])  - 1

            if has_down and has_up and has_left and has_right:
                count += 1

        
        return count
