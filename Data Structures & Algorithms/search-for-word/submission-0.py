class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()
        def backtrack(start, i):
            if i == len(word):
                return True
            x = start[0]
            y = start[1]
            if (x < 0 or y < 0 or x >= row or y >= col or word[i] != board[x][y] or (x, y) in path):
                return False
            path.add((x, y))
            res = backtrack((x-1, y), i+1) or backtrack((x+1, y), i+1) or backtrack((x, y-1), i+1) or backtrack((x, y+1), i+1)
            path.remove((x,y))
            return res

        for x in range(row):
            for y in range(col):
                if backtrack((x,y), 0):
                    return True

        return False