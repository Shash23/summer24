class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        directions = [-1, 0, 1]

        queue = deque()

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        # initial source
        for i in range(m):

            visited[i][0] = True
            # row, column, move
            queue.append((i, 0, 0))

        num_moves = 0

        while queue:

            length = len(queue)

            for i in range(length):

                row, col, moves = queue.popleft()

                num_moves = max(num_moves, moves)

                for direction in directions:

                    new_row = row + direction
                    new_col = col + 1
                    # print(new_row, new_col)
                    
                    if( 0 <= new_row < m and 0 <= new_col < n  and not visited[new_row][new_col] and grid[row][col] < grid[new_row][new_col]):
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col, moves + 1))


        return num_moves