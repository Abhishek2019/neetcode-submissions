
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        out = {}
        for idx in range(len(numbers)):

            i = numbers[idx]

            if i not in out:
                out[target-i] = idx
                # print(out)
            else:
                return [out[i]+1,idx+1]

        