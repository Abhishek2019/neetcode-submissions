from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):

                ele = board[row_idx][col_idx]

                if ele == ".":
                    continue

                if ele in row_check[row_idx]:
                    return False
                
                if ele in col_check[col_idx]:
                    return False
                
                key = [(row_idx)//3, (col_idx)//3]
                if ele in box_check[tuple(key)]:
                    return False

                
                row_check[row_idx].add(ele)
                col_check[col_idx].add(ele)
                box_check[tuple(key)].add(ele)
            
        return True
        
