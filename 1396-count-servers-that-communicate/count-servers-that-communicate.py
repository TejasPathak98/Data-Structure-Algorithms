class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        connected_servers = 0
        visited_server = set()


        for i in range(m):
            visited_server_row = set()
            servers_in_row = 0
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                else:
                    visited_server_row.add((i,j))
                    servers_in_row += 1
            
            if servers_in_row > 1:
                connected_servers += servers_in_row
                visited_server.update(visited_server_row)

        for j in range(n):
            servers_in_col = 0
            row_visited_server_count = 0
            for i in range(m):
                if grid[i][j] == 0:
                    continue
                else:
                    if (i,j) in visited_server:
                        row_visited_server_count += 1
                    else:
                        servers_in_col += 1
            
            if row_visited_server_count + servers_in_col > 1:
                connected_servers += servers_in_col

        return connected_servers



