class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        selected_row = -1

        for i in range(len(matrix)):

            if matrix[i][0]<=target<=matrix[i][-1]:
                selected_row = i
                break

        if selected_row == -1:
            return False

        l = 0
        r = len(matrix[selected_row])

        while l<=r:

            mid = (l+r)//2

            if target == matrix[selected_row][mid]:
                return True

            elif matrix[selected_row][mid]>target:

                r = mid-1

            else:
                l = mid+1


        return False