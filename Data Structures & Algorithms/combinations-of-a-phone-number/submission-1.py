class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        out = []
        if not digits:
            return out


        def dfs(i,arr):

            print(arr)
            if i == len(digits):
                out.append("".join(arr))
                return

            for ch in map[int(digits[i])]:

                arr.append(ch)
                dfs(i+1,arr)
                arr.pop()

        dfs(0, [])
        return out


















