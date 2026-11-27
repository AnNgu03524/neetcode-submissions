class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_map = collections.defaultdict(set)
        row_map = collections.defaultdict(set)
        square_map = collections.defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]

                # skip invalid chars '.'
                if val == ".":
                    continue
                
                if  (val in row_map[i] or
                    val in col_map[j] or
                    val in square_map[(i // 3, j // 3)]):
                    return False
                row_map[i].add(val)
                col_map[j].add(val)
                square_map[(i // 3, j // 3)].add(val)

        return True
                  

            

            

                
                