class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        first_idx = 0
        current = None
        while first_idx<len(triplets):
            if triplets[first_idx][0]<=target[0] and triplets[first_idx][1]<=target[1] and triplets[first_idx][2] <= target[2]:
                current = triplets[first_idx]
                break

            first_idx+=1

        if not current:
            return False

        if current == target:
            return True

        for idx in range(first_idx+1,len(triplets)):

            b = triplets[idx]

            if b[0]<=target[0] and b[1]<=target[1] and b[2] <= target[2]:

                current[0] = max(b[0], current[0])
                current[1] = max(b[1], current[1])
                current[2] = max(b[2], current[2])


                if current == target:
                    return True


        return False


