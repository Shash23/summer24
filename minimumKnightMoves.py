class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        if x == 0 and y == 0:
            return 0

        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        
        def bfs(x, y):

            visited = set()
            q = collections.deque([(0,0)])
            moves = 0

            while q:

                neighbor_cnt = len(q)

                for i in range(neighbor_cnt):

                    px, py = q.popleft()

                    if(px, py) == (x, y):
                        return moves

                    for dx, dy in directions:
                        nx, ny = px + dx, py + dy

                        if(nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))

                moves += 1

        return bfs(x,y)