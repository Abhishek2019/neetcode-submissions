class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        search_list = []
        for row in matrix:

            if target <= row[-1]:

                search_list = row
                break

        if not search_list:
            return False

        
        l = 0
        r = len(search_list)-1

        while l<=r:

            mid = (l+r)//2

            if search_list[mid] == target:
                return True
            
            elif search_list[mid] > target:
                r=mid-1
            else:
                l = mid+1
                

        return False





